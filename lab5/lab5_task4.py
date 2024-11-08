import doctest

def credit_flyweight(food_ate):
	return food_ate * 10;

def credit_strawweight(food_ate):
	return food_ate * 15;

def my_food_credit(food_ate: float, opp_food_ate: float) -> float:
	"""
	My food credit.
	"""

	assert type(food_ate) == float, "invalid"
	assert type(opp_food_ate) == float, "invalid"

	assert food_ate >= 0, "invalid"
	assert opp_food_ate >= 0, "invalid"

	my_credit = credit_flyweight(food_ate)
	opponent_credit = credit_strawweight(opp_food_ate)

	my_credit -= 0.2 * opponent_credit
	if my_credit < 0:
		my_credit = 0
	return my_credit


def opponent_food_credit(opp_food_ate: float, food_ate: float) -> float:
	"""
	Opponent food credit.
	"""

	assert type(opp_food_ate) == float, "invalid"
	assert type(food_ate) == float, "invalid"

	assert opp_food_ate >= 0, "invalid"
	assert food_ate >= 0, "invalid"

	opponent_credit = credit_strawweight(opp_food_ate)
	my_credit = credit_flyweight(food_ate)

	opponent_credit -= 0.2 * my_credit
	if opponent_credit < 0:
		opponent_credit = 0
	return opponent_credit

if __name__ == "__main__":
	doctest.testmod()
