"""Web server for the hog GUI."""
import io
import os
import logging
from contextlib import redirect_stdout

from gui_files.common_server import route, start

import hog
import dice
import default_graphics

PORT = 31415
DEFAULT_SERVER = "https://hog.cs61a.org"
GUI_FOLDER = "gui_files/"
PATHS = {}


class HogLoggingException(Exception):
    pass


@route
def take_turn(prev_rolls, move_history, goal, game_rules):
    """Simulate the whole game up to the current turn."""
    fair_dice = dice.make_fair_dice(6)
    dice_results = []

    hog_pile = game_rules["Hog Pile"]

    try:
        old_hog_pile = hog.hog_pile
        if not hog_pile:
            hog.hog_pile = lambda score0, score1: 0

        def logged_dice():
            if len(dice_results) < len(prev_rolls):
                out = prev_rolls[len(dice_results)]
            else:
                out = fair_dice()
            dice_results.append(out)
            return out

        final_scores = None
        final_message = None
        who = 0

        commentary = hog.both(
            hog.say_scores,
            hog.announce_lead_changes,
        )

        def log(*logged_scores):
            nonlocal final_message
            leader, message = commentary(*logged_scores)
            final_message = message
            return leader, message

        move_cnt = 0

        def strategy_for(player):
            def strategy(*scores):
                nonlocal final_scores, move_cnt, who
                final_scores = scores
                if player:
                    final_scores = final_scores[::-1]
                who = player
                if move_cnt == len(move_history):
                    raise HogLoggingException()
                move = move_history[move_cnt]
                move_cnt += 1
                return move

            return strategy

        game_over = False

        try:
            final_scores = trace_play(
                hog.play,
                strategy_for(0),
                strategy_for(1),
                0,
                0,
                dice=logged_dice,
                say=log,
                goal=goal,
            )[:2]
        except HogLoggingException:
            pass
        else:
            game_over = True
    finally:
        hog.hog_pile = old_hog_pile

    return {
        "rolls": dice_results,
        "finalScores": final_scores,
        "message": final_message,
        "gameOver": game_over,
        "who": who,
    }


@route
def strategy(name, scores):
    STRATEGIES = {
        "hefty_hogs_strategy": hog.hefty_hogs_strategy,
        "hog_pile_strategy": hog.hog_pile_strategy,
        "final_strategy": hog.final_strategy,
    }
    return STRATEGIES[name](*scores[::-1])


@route("dice_graphic.svg")
def draw_dice_graphic(num, no_default=False):
    num = int(num[0])
    # Either draw student-provided dice or our default dice
    try:
        import design
        if hasattr(design, "draw_dice") or no_default:
            graphic = design.draw_dice(num)
            return str(graphic)
    except ModuleNotFoundError:
        pass
    return default_graphics.dice[num]


def trace_play(play, strategy0, strategy1, score0, score1, dice, goal, say):
    """Wraps the user's play function and
        (1) ensures that strategy0 and strategy1 are called exactly once per turn
        (2) records the entire game, returning the result as a list of dictionaries,
            each with keys "s0_start", "s1_start", "who", "num_dice", "dice_values"
    Returns (s0, s1, trace) where s0, s1 are the return values from play and trace
        is the trace as specified above.
    This might seem a bit overcomplicated but it will also used to create the game
        traces for the fuzz test (when run against the staff solution).
    """
    game_trace = []

    def mod_strategy(who, my_score, opponent_score):
        if game_trace:
            prev_total_score = game_trace[-1]["s0_start"] + game_trace[-1]["s1_start"]
            if prev_total_score == my_score + opponent_score:
                # game is still on last turn since the total number of points
                # goes up every turn
                return game_trace[-1]["num_dice"]
        current_num_dice = (strategy0, strategy1)[who](my_score, opponent_score)
        current_turn = {
            "s0_start": [my_score, opponent_score][who],
            "s1_start": [my_score, opponent_score][1 - who],
            "who": who,
            "num_dice": current_num_dice,
            "dice_values": [],  # no dice rolled yet
        }
        game_trace.append(current_turn)
        return current_num_dice

    def mod_dice():
        roll = dice()
        if not game_trace:
            raise RuntimeError("roll_dice called before either strategy function")
        game_trace[-1]["dice_values"].append(roll)
        return roll

    f = io.StringIO()
    with redirect_stdout(f):
        s0, s1 = play(
            lambda a, b: mod_strategy(0, a, b),
            lambda a, b: mod_strategy(1, a, b),
            score0,
            score1,
            dice=mod_dice,
            goal=goal,
            say=say,
        )
    return s0, s1, game_trace


if __name__ == "__main__" or "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    print("Starting the server...") 
    app = start(PORT, DEFAULT_SERVER, GUI_FOLDER)
    print(f"Server is running on http://localhost:{PORT}/") 
