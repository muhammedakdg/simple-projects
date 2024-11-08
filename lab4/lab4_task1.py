import doctest

def fruit_price(num_apples: int, num_peaches: int, num_watermelon: int) -> float:
	"""
	Return the total price given the number of each fruit to purchase.

	>>> fruit_price(1, 2, 3)
	34.89
	>>> fruit_price(0, 0, 0)
	0.0
	>>> fruit_price(1.5, 2, 3)
	Traceback (most recent call last):
	...
	AssertionError: invalid data type of num_apples
	>>> fruit_price(3, '2', 5)
	Traceback (most recent call last):
	...
	AssertionError: invalid data type of num_peaches
	>>> fruit_price(1, -3, -5)
	Traceback (most recent call last):
	...
	AssertionError: num_peaches should be non-negative
	>>> fruit_price(1, -3, -5.5)
	Traceback (most recent call last):
	...
	AssertionError: invalid data type of num_watermelons
	"""

	assert type(num_apples) == int, "invalid data type of num_apples"
	assert type(num_peaches) == int, "invalid data type of num_peaches"
	assert type(num_watermelon) == int, "invalid data type of num_watermelons"

	assert num_apples >= 0, "num_apples should be non-negative"
	assert num_peaches >= 0, "num_peaches should be non-negative"
	assert num_watermelon >= 0, "num_watermelon should be non-negative"

	# specify fruit unit price
	price_apples = 2.94
	price_peaches = 3.99
	price_watermelon = 7.99

	# calculate the total price
	total_price = price_apples * num_apples + price_peaches * num_peaches + price_watermelon * num_watermelon

	# return the total price
	return total_price

doctest.testmod()
