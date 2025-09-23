def is_perfect_square(number):
	if not isinstance(number, int):
		raise ValueError("Input must be an integer")
	return number ** 0.5 % 1 == 0
			
		
def get_perfect_square(number_list):
	if not isinstance(number_list, list):
		raise TypeError("list_of_numbers must be a list")
	if all(type(item) != int for item in number_list):
			raise ValueError("list_of_numbers must all be integers")
	perfect_squares = list(map(is_perfect_square, number_list))
	return perfect_squares

		
ages = [2, 3, 4, 5, 9, 25]	



print(get_perfect_square(ages))







