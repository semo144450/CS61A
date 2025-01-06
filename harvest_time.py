"""This function should return true
if the month is July OR the tuber size is at least 2 feet. 
"""
def harvest_time(month, tuber_size):
    """
    >>> harvest_time("May", 1)
    False
    >>> harvest_time("May", 2)
    True
    >>> harvest_time("May", 3)
    True
    >>> harvest_time("July", 1)
    True
    >>> harvest_time("July", 2)
    True
    >>> harvest_time("July", 4)
    True
    """
    return (month == "July") or (tuber_size >= 2)