import doctest

def absolute_value(expression: str) -> float:
	"""
	Evaluates an absolute value expression.

	>>> absolute_value("|0|")
	0.0
	>>> absolute_value("|1|")
	1.0
	>>> absolute_value("|-1|")
	1.0
	>>> absolute_value("|-3.5|")
	3.5
	"""

	assert type(expression) == str, "invalid"
	expression = expression.strip()
	assert expression != "", "invalid"

	assert expression[0] == "|", "invalid"
	assert expression[-1] == "|", "invalid"

	assert expression.count("|") == 2, "invalid"
	assert expression.count(".") <= 1, "invalid"

	expression = expression[1:-1].strip()
	assert expression != "", "invalid"

	if expression[0] == "-":
		expression = expression[1:]

	decimal_index = expression.find(".")
	if decimal_index == -1:
		assert expression.isnumeric(), "invalid"
	else:
		assert expression[0:decimal_index].isnumeric(), "invalid"
		assert expression[decimal_index + 1:].isnumeric(), "invalid"

	return float(expression)

if __name__ == "__main__":
	doctest.testmod()
