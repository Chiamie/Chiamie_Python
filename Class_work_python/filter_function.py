def is_even(number):
	if not isinstance(number, int):
		raise ValueError("Input must be an integer")
	return number % 2 == 0
		
	
numbers = [1, 2, 3, 4, 5]

def get_is_even_of(number_list):
	if not isinstance(number_list, list):
		raise TypeError("list_of_numbers must be a list")
	if all(type(item) != int for item in number_list):
			raise ValueError("list_of_numbers must all be integers")
	new_list = list(filter(is_even, number_list))
	return new_list



print(get_is_even_of(numbers))

	
