"""Write a function that will count the amount of multiples
of a given divisor between a given start number and a given end number.
It should include the start or end if they are a multiple.

For example, if the range is 1 to 12 and the divisor is 3,
the function should return 4, since 3, 6, 9, and 12 can all be evenly divided by 3.
"""
from operator import floordiv


def count_multiples(start, end, divisor):
    """
    >>> count_multiples(2, 2, 1)       # 2 is a multiple of 1
    1
    >>> count_multiples(2, 2, 2)       # 2 is a multiple of 2
    1
    >>> count_multiples(2, 2, 3)       # 2 is not a multiple of 3
    0
    >>> count_multiples(1, 12, 3)      # 3, 6, 9, 12
    4
    >>> count_multiples(237, 500, 10)
    27
    """
    # YOUR CODE HERE
    num1 = floordiv(start, divisor)
    num2 = floordiv(end, divisor)
    if start != end:
        return num2 - num1
    elif start % divisor == 0:
        return 1
    else:
        return 0
