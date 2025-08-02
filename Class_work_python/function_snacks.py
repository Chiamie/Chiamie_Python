def divide_or_square(number):
	if type(number) == str:
		raise ValueError("invalid data")
	elif number < 0:
		raise ValueError("invalid data")
	if number % 5 == 0:
		return round((number ** 0.5), 2)
	else:
		return number % 5
	


def future_investment(investment_amount, monthly_interestRate, years):
	if type(investment_amount) == str or type(monthly_interestRate) == str or type(years) == str:
		raise ValueError("invalid data")
	if investment_amount == 0 or monthly_interestRate == 0 or years == 0:
		raise ValueError("invalid data")
	if investment_amount < 0 or monthly_interestRate < 0 or years < 0:
		raise ValueError("invalid data")
	number_of_months = years * 12
	future_investment_value = investment_amount * ((1 + monthly_interestRate) ** number_of_months)
	return future_investment_value



def only_floats(number1, number2):
	if type(number1) == float and type(number2) == float:
		return 2
	elif type(number1) == float and type(number2) != float:
		return 1
	elif type(number1) != float and type(number2) != float:
		return 0
	elif number1 == "" or number2 == "":
		raise ValueError("invalid data")
	elif number1 < 0.0  or number2 < 0.0:
		raise ValueError("invalid data")
