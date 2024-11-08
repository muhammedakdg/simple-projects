import doctest

def count_wheels(num_bicycles: int, num_tricycles: int, num_cars: int, num_trucks: int) -> int:
    """
    Return the total number of wheels.

    >>> count_wheels(1, 1, 1, 1)
    27
    >>> count_wheels(4, 3, 2, 1)
    43
    >>> count_wheels(1, 2, 3, 1)
    38
    >>> count_wheels(2, 2, 2, 2)
    54
    """
    #pass

    assert type(num_bicycles) == int, "invalid data type of num_bicycles"
    assert type(num_tricycles) == int, "invalid data type of num_tricycles"
    assert type(num_cars) == int, "invalid data type of num_cars"
    assert type(num_trucks) == int, "invalid data type of num_trucks"

    assert num_bicycles >= 0, "num_bicycles should be non-negative"
    assert num_tricycles >= 0, "num_tricycles should be non-negative"
    assert num_cars >= 0, "num_cars should be non-negative"
    assert num_trucks >= 0, "num_trucks should be non-negative"

    bicycle_wheels = 2 * num_bicycles
    tricycle_wheels = 3 * num_tricycles
    car_wheels = 4 * num_cars
    truck_wheels = 18 * num_trucks
    total_wheels = bicycle_wheels + tricycle_wheels + car_wheels + truck_wheels
    return total_wheels

doctest.testmod()
