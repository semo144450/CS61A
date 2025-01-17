 # Q1: Warm Up: Recursive Multiplication
 def multiply(m, n):
    """ Takes two positive integers and returns their product using
    recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n- 1)


# Q2: Recursion Environment Diagram
def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
# >>rec(3, 2)


# Find the Bug Q3：找到 Bug
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)


# Q4: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
    return 1
    elif n % 2 == 0:
    return 1 + hailstone(n // 2)
    else:
    return 1 + hailstone(3 * n + 1)


# Q5: Merge Numbers
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1

    n1, n1_last = n1 // 10, n1 % 10
    n2, n2_last = n2 // 10, n2 % 10
 
    if n1_last > n2_last:
        return n1_last * 10 + n2_last + 100 * merge(n1, n2)
    else:
        return n2_last * 10 + n1_last + 100 * merge(n1, n2)
    """
    降一位
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    """


# Q6: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        else:
            return helper(i + 1)
    return helper(2)

