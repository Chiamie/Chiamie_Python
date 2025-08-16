def getSquaresOf(number):
	if not isinstance(number, int):
		raise ValueError("Input must be an integer")
	return number ** 2
		
	
numbers = [1, 2, 3, 4, 5]

def square(number_list):
	if not isinstance(number_list, list):
		raise TypeError("list_of_numbers must be a list")
	if all(type(item) != int for item in number_list):
			raise ValueError("list_of_numbers must all be integers")
	squares = list(map(getSquaresOf, number_list))
	return squares



print(square(numbers))













