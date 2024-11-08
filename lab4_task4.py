import doctest

def need_to_buy_ticket(age: float, height: float) -> bool:
    """
    Returns true if the given person needs to buy a ticket.

    >>> need_to_buy_ticket(7, 130)
    True
    >>> need_to_buy_ticket(5, 110)
    False
    >>> need_to_buy_ticket(7, 110)
    True
    >>> need_to_buy_ticket(5, 130)
    True
    """
    #pass

    assert type(age) == int or type(age) == float, "invalid data type of age"
    assert type(height) == int or type(height) == float, "invalid data type of height"

    assert age > 0, "age must be nonnegative"
    assert height > 0, "height must be nonnegative"

    return height > 120 or age > 6

doctest.testmod()
