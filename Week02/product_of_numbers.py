"""
This function should return the product 
of all the numbers from 1 to the given end number
(including the end number).

It is mostly written for you, but it has several bugs!
Tips for debugging:
* Read through the code and trace it on paper for small inputs
* Try running the tests and observe the output
* If you have a hunch, try changing the code and seeing how the output changes
"""


def product_of_numbers(end):
    """
    >>> product_of_numbers(1)
    1
    >>> product_of_numbers(2)
    2
    >>> product_of_numbers(3)
    6
    >>> product_of_numbers(10)
    3628800
    """
    result = 1
    counter = 1
    while counter < end:
        counter += 1
        result *= counter
    return result
