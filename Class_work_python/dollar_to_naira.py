def get_dollar_amount(number):
	if type(number) == str:
		raise ValueError("invalid value")
	return number * 1550