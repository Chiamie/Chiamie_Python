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
def is_palindrome(number):
	if number == number[::-1]:
		return number

		
def get_all_palindomes_of(list_of_strings):
	palindromes_of_list = list(filter(is_palindrome, list_of_strings))
	return palindromes_of_list
words = ['level', 'world', 'madam', 'python']
print(get_all_palindomes_of(words))


#Section Four: Question 1
def get_uppercase_of(word):
	return word.upper()

		
def get_all_to_uppercase(list_of_strings):
	uppercase_of_list = list(map(get_uppercase_of, list_of_strings))
	return uppercase_of_list
words = ['level', 'world', 'madam', 'python', 'c++']
print(get_all_to_uppercase(words))


#Section Four: Question 2
def get_square_of(number):
	return number ** 2

		
def get_each_element_square_of(list_of_numbers):
	square_of_list = list(map(get_square_of, list_of_numbers))
	return square_of_list
grades = range(1, 10)
print(get_each_element_square_of(grades))



#Section Four: Question 3
def capiltalize_first_letter(word):
	return word.capitalize()

		
def capiltalize_first_letter_of(list_of_words):
	each_element_capitalized_of_list = list(map(capiltalize_first_letter, list_of_words))
	return each_element_capitalized_of_list
names = ['john', 'mary','steve']
print(capiltalize_first_letter_of(names))



#Section Four: Question 4
def get_10_percent_tax_of(number):
	number += number * 10/100
	return number

		
def get_10_percent_tax_each_of(list_of_numbers):
	tax_of_10_percent_of_list = list(map(get_10_percent_tax_of, list_of_numbers))
	return tax_of_10_percent_of_list
prices = [100, 200, 300]
print(get_10_percent_tax_each_of(prices))



#Section Five: Question 1
from functools import reduce
def get_sum_of(number, number1):
	return number + number1

		
def get_sum_of_each_of(list_of_numbers):
	sum_of_element_of_list = reduce(get_sum_of, list_of_numbers)
	return sum_of_element_of_list
prices = [100, 200, 300]
print(get_sum_of_each_of(prices))


#Section Five: Question 2 
def get_maximum_of(number, number1):
	return max(number, number1)

		
def get_maximum_element_of(list_of_numbers):
	maximum_element_of_list = reduce(get_maximum_of, list_of_numbers)
	return maximum_element_of_list
prices = [100, 500, 300]
print(get_maximum_element_of(prices))



#Section Five: Question 3 
def merge_element_of(word, word1):
	word += " " + word1
	return word

		
def merge_each_element_of(list_of_strings):
	merged_element_of_list = reduce(merge_element_of, list_of_strings)
	return merged_element_of_list
words = ['I', 'love', 'Python']
print(merge_each_element_of(words))



#Section Five: Question 4 
def get_squares_of(number):
	return number ** 2

def get_product_of(number, number1):
	number *= number1
	return number
		
def get_product_of_squares_of_each_element_of(list_of_numbers):
	squared_element_of_list = list(map(get_squares_of, list_of_numbers))
	product_of_all_elements_of_list = reduce(get_product_of, squared_element_of_list)
	return product_of_all_elements_of_list

numbers = [1, 2, 3, 4]
print(get_product_of_squares_of_each_element_of(numbers))



#Section Six: Question 1 
def get_sum_of(list_of_tuples):
	sum_list = []
	for number in range(len(list_of_tuples)):
		sum = 0
		for index in range(len(list_of_tuples[number])):
			sum += list_of_tuples[number][index]
		sum_list.append(sum)
	return sum_list


numbers = [(1, 2), (3, 4), (5, 6)]
print(get_sum_of(numbers))



#Section Six: Question 2 
def is_numeric_strings(number):
	return number.isnumeric()

def get_numeric_strings_of(list_of_strings):
	numeric_strings_of_list = list(filter(is_numeric_strings, list_of_strings))
	return numeric_strings_of_list


data = ['123', '456', '789', 'abc', 'def']
print(get_numeric_strings_of(data))



