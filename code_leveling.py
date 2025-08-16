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
def getSumOf(list_of_list_of_numbers):
	list_of_length = []
	for index in range(0, len(list_of_list_of_numbers)):
		sum = 0
		for number in range(0, len(list_of_list_of_numbers[index])):
			sum += list_of_list_of_numbers[index][number]
		list_of_length.append(sum)
	return list_of_length



scores = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(getSumOf(scores))


#Section Two: Question 2
def getSumOf(list_of_list_of_numbers):
	list_of_length = []
	for index in range(0, len(list_of_list_of_numbers)):
		sum = 0
		for number in range(0, len(list_of_list_of_numbers[index])):
			sum += list_of_list_of_numbers[number][index]
		list_of_length.append(sum)
	return list_of_length



scores = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(getSumOf(scores))


#Section Three: Question 1
def is_even(number):
	return number % 2 == 0

def get_all_even_numbers_of(number_list):
	even_numbers_of_list = list(filter(is_even, number_list))
	return even_numbers_of_list

scores = [2, 3, 4, 1, 5, 7, 4, 6, 8]
print(get_all_even_numbers_of(scores))


#Section Three: Question 2
def is_five_characters(word):
	return len(word) == 5

def extract_words_of_5_charcters_of(word_list):
	words_of_5_charcters = list(filter(is_five_characters, word_list))
	return words_of_5_charcters

animals = ['cat', 'elephant', 'tiger', 'lion', 'amaka']
print(extract_words_of_5_charcters_of(animals))



#Section Three: Question 3
def is_greater_than_two_of(number):
	return number[0] > 2

		
def remove_tuples_with_number_less_than_2_in(tuple_list):
	tuples_with_number_greater_than_2 = list(filter(is_greater_than_two_of, tuple_list))
	return tuples_with_number_greater_than_2

grades = [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A')]
print(remove_tuples_with_number_less_than_2_in(grades))

	
	
	
	
#Section Three: Question 4
def is_divisible_by_both_3_and_5_of(number):
	if number % 3 == 0 and number % 5 == 0:
		return number

		
def get_number_divisible_by_3_and_5_in(range_of_numbers):
	number_divisible_by_3_and_5 = list(filter(is_divisible_by_both_3_and_5_of, range_of_numbers))
	return number_divisible_by_3_and_5
grades = range(1, 51)
print(get_number_divisible_by_3_and_5_in(grades))





#Section Three: Question 5
def is_divisible_by_both_3_and_5_of(number):
	if number % 3 == 0 and number % 5 == 0:
		return number

		
def get_number_divisible_by_3_and_5_in(range_of_numbers):
	number_divisible_by_3_and_5 = list(filter(is_divisible_by_both_3_and_5_of, range_of_numbers))
	return number_divisible_by_3_and_5
grades = range(1, 51)
print(get_number_divisible_by_3_and_5_in(grades))



		














