""""
Write a function that sums up the multiples of a given number between a given start and end.
If the start or end numbers are also multiples, it should include them in the sum.

For example, if the range is 1-12 and the divisor is 4, the function should add 4+8+12, returning 24.
"""
from operator import floordiv, mul


def sum_multiples(start, end, divisor):
    """
    >>> sum_multiples(1, 12, 4)
    24
    >>> sum_multiples(1, 12, 13)
    0
    >>> sum_multiples(2, 2, 2)
    2
    >>> sum_multiples(2, 2, 3)
    0
    >>> sum_multiples(23, 81, 13)
    260
    """
    # YOUR CODE HERE
    num1 = floordiv(start, divisor)
    if start == end:
        if floordiv(start, divisor) == 0:
            return 0
        else:
            return start
    else:
        test = mul(num1, divisor)
        count = 0
        while test < end:
            test = test + divisor
            if test <= end:
                count = count + test
        return count
