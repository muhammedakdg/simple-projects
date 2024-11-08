import doctest

Pi = 3.14159

def circle_area(radius: float) -> float:
	"""
	pi * r ** 2

	The radius is in the range 0.0 to 1000.0.

	>>> circle_area(2.0)
	12.56636
	>>> circle_area(4.0)
	50.26544
	"""

	assert type(radius) == float, "radius must be a float."
	assert 0 <= radius <= 1000, "radius must be in the range [0.0, 1000.0]"

	return Pi * radius**2

def circle_circumference(radius: float) -> float:
	"""
	2 * pi * r

	The radius is in the range 0.0 to 1000.0.

	>>> circle_circumference(2.0)
	12.56636
	>>> circle_circumference(4.0)
	25.13272
	"""

	assert type(radius) == float, "radius must be a float"
	assert 0 <= radius <= 1000, "radius must be in the range [0.0, 1000.0]"

	return 2 * Pi * radius

doctest.testmod()
