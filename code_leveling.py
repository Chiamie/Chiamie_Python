#Question 1
tuple_of_numbers = (2, 4, 1, 7, 8)

tuple_of_numbers += (1, )
print(tuple_of_numbers)


#Question 2

numbers = (1, 2, [3, 4], 5)
numbers[2][1] = 99
print(numbers)


#Question 3
tuple_of_strings = ('apple', 'banana', 'cherry')
list_of_strings = []
for items in tuple_of_strings:
	list_of_strings.append(items)
print(list_of_strings)
list_of_strings.append('mango')
print(list_of_strings)
new_tuple_of_strings = tuple(list_of_strings)
print(new_tuple_of_strings)


#Question 4
tuple_of_numbers = (10, 20, 30, 40)
a, b, *c = tuple_of_numbers
print(a, b, c)


#Section Two: Question 1
def get_the_total_of(list_of_list_of_numbers):
	if not all(isinstance(sublist, list) for sublist in list_of_list_of_numbers):
		raise TypeError("Input must be a list of lists")
	
	if not all(isinstance(item, (int, float)) for sublist in list_of_list_of_numbers for item in sublist):
		raise ValueError("list_of_numbers must all be integers or floats")
		
	for sublist in list_of_list_of_numbers:
		for item in sublist:
			if item < 0:
				raise ValueError("list_of_numbers must all be positive integers or positive floats")
				
	if list_of_list_of_numbers == []:
		raise ValueError("list_of_list_of_numbers cannot be empty")

	list_of_length = []
	for index in range(0, len(list_of_list_of_numbers)):
		sum = 0
		for number in range(0, len(list_of_list_of_numbers[index])):
			sum += list_of_list_of_numbers[index][number]
		list_of_length.append(sum)
	return list_of_length



scores = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(get_the_total_of(scores))


#Section Two: Question 2
def get_sum_of(list_of_list_of_numbers):
	if not all(isinstance(sublist, list) for sublist in list_of_list_of_numbers):
		raise TypeError("Input must be a list of lists")
		
	if not all(isinstance(item, (int, float)) for sublist in list_of_list_of_numbers for item in sublist):
		raise ValueError("list_of_numbers must all be integers or floats")
		
	for sublist in list_of_list_of_numbers:
		for item in sublist:
			if item < 0:
				raise ValueError("list_of_numbers must all be positive integers or positive floats")
				
	if list_of_list_of_numbers == []:
		raise ValueError("list_of_list_of_numbers cannot be empty")
		
	list_of_length = []
	for index in range(0, len(list_of_list_of_numbers)):
		sum = 0
		for number in range(0, len(list_of_list_of_numbers[index])):
			sum += list_of_list_of_numbers[number][index]
		list_of_length.append(sum)
	return list_of_length



scores = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(get_sum_of(scores))



	



	
	
	
