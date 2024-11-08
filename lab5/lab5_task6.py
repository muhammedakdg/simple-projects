import doctest

def is_even(number: int) -> bool:
	"""
	Returns true if the number is even.

	>>> is_even(0)
	True
	>>> is_even(2)
	True
	>>> is_even(3)
	False
	>>> is_even(-3)
	False
	"""

	assert type(number) == int, "invalid"

	return number % 2 == 0

if __name__ == "__main__":
	doctest.testmod()
