import doctest
import re

def pound(expression: str) -> int:
	"""
	Return the result of the pound operation that is defined as "x # y" = x^2 - y^2

	>>> pound("2 # 3")
	-5
	>>> pound("0 # 0")
	0
	>>> pound("6 # 1")
	35
	>>> pound(5)
	Traceback (most recent call last):
	...
	AssertionError: invalid argument type
	"""

	assert type(expression) == str, "invalid argument type"
	assert expression.count("#") == 1, "invalid"

	# Do some calculation with the input
	# 1 Find x and y in "x # y"
	# 1.1 Find where '#' is 
	expression = expression.strip()
	#expression = re.sub("##+", "#", expression)
	pound_index = expression.find('#')

	# 1.2Find what the number is before '#' and let it be x
	x_str = expression[:pound_index].strip()
	assert x_str.isdigit(), "invalid"
	x = int(x_str)

	# 1.3Find what the number is before '#' and let it be y
	y_str = expression[pound_index + 1:].strip()
	assert y_str.isdigit(), "invalid"
	y = int(y_str)

	# 2 Calculate the result based on the definition of '#'
	# which is x # y = x2 – y2 
	result = x * x - y * y

	# Show the result
	return result

#print(pound(" # 811"))

doctest.testmod()
