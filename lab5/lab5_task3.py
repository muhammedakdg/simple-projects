import doctest

def get_store1_revenue(store1_monthly_sales: float) -> float:
	assert type(store1_monthly_sales) == float, "invalid"
	assert store1_monthly_sales >= 0, "invalid"
	return store1_monthly_sales / 5

def get_store2_revenue(store2_monthly_sales: float) -> float:
	assert type(store2_monthly_sales) == float, "invalid"
	assert store2_monthly_sales >= 0, "invalid"
	return store2_monthly_sales / 8

def get_total_revenue(store1_monthly_sales: float, store2_monthly_sales: float) -> float:
	"""
	Returns the total revenue.

	>>> get_total_revenue(100.0, 200.0)
	45.0
	>>> get_total_revenue(200.0, 100.0)
	52.5
	>>> get_total_revenue(100.0, 0.0)
	20.0
	>>> get_total_revenue(200.0, 0.0)
	40.0
	"""

	assert type(store1_monthly_sales) == float, "invalid"
	assert type(store2_monthly_sales) == float, "invalid"

	assert store1_monthly_sales >= 0, "invalid"
	assert store2_monthly_sales >= 0, "invalid"

	profit1 = get_store1_revenue(store1_monthly_sales)
	profit2 = get_store2_revenue(store2_monthly_sales)
	return profit1 + profit2

if __name__ == "__main__":
	doctest.testmod()
