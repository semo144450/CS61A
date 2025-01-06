"""
Write a function that will count the number of even numbers between a given start number and a given end number.
It should include the start or end if they are even.
"""
from operator import floordiv, sub


def count_evens(start, end):
    """
    >>> count_evens(2, 2)
    1
    >>> count_evens(-2, 52)
    28
    >>> count_evens(237, 500)
    132
    """
    # YOUR CODE HERE
    count = 0
    if start % 2 == 0:
        count += 1
    count += floordiv(sub(end, start) - 1, 2)
    if end % 2 == 0:
        count += 1
    return count
