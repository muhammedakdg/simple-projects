import doctest

def xor_operator(one: bool, two: bool) -> bool:
	"""
	Returns true if only one of the given parameters is true.

	>>> xor_operator(True, True)
	False
	>>> xor_operator(True, False)
	True
	>>> xor_operator(False, True)
	True
	>>> xor_operator(False, False)
	False
	"""

	assert type(one) == bool, "invalid data type of one"
	assert type(two) == bool, "invalid data type of two"

	return one != two

doctest.testmod()
