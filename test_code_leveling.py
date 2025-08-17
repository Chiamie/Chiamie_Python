import unittest
import code_leveling



class TestGetTheTotalOfFunction(unittest.TestCase):
	def test_that_get_the_total_of_function_receives_a_list_of_list_as_input(self):
		list_of_numbers = [[1, 5, 2], [3, 7, 4], [5, 8, 6]]
		result = code_leveling.get_the_total_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_the_total_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_the_total_of, "not a list")
	def test_that_the_get_the_total_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = [['name', 'amaka', 'ayo'], ['awele', 'nutrient', 'plate']]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_a_list_contains_non_numeric(self):
		list_of_integers = [[1, 5, 2], [3, 7, 4], [5, 'a', 6]]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_a_sublist_has_negative_number(self):
		list_of_integers = [[1, 5, -2], [3, 7, 4], [5, 8, 6]]
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_the_total_of, list_of_integers)
	def test_that_the_get_the_total_of_function_returns_correct_result(self):
		result = code_leveling.get_the_total_of([[1, 5, 2], [3, 7, 4], [5, 8, 6]])
		self.assertEqual(result, [8, 14, 19])



class TestGetSumOfFunction(unittest.TestCase):
	def test_that_the_get_sum_of_function_receives_a_list_of_list_as_input(self):
		list_of_numbers = [[1, 5, 2], [3, 7, 4], [5, 8, 6]]
		result = code_leveling.get_sum_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_sum_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_sum_of, "not a list")
	def test_that_the_get_sum_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = [['name', 'amaka', 'ayo'], ['awele', 'nutrient', 'plate']]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_a_list_contains_non_numeric(self):
		list_of_integers = [[1, 5, 2], [3, 7, 4], [5, 'a', 6]]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_a_sublist_has_negative_number(self):
		list_of_integers = [[1, 5, -2], [3, 7, 4], [5, 8, 6]]
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_sum_of, list_of_integers)
	def test_that_the_get_sum_of_function_returns_correct_result(self):
		result = code_leveling.get_sum_of([[1, 5, 2], [3, 7, 4], [5, 8, 6]])
		self.assertEqual(result, [9, 20, 12])



class TestGetAllEvenNumbersOfFunction(unittest.TestCase):
	def test_that_the_get_even_numbers_of_function_receives_a_list_as_input(self):
		list_of_numbers = [1, 5, 3, 7, 8, 6]
		result = code_leveling.get_all_even_numbers_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_even_numbers_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_all_even_numbers_of, "not a list")
	def test_that_the_get_even_numbers_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = ['awele', 'nutrient', 'plate']
		self.assertRaises(ValueError, code_leveling.get_all_even_numbers_of, list_of_integers)		
	def test_that_the_get_even_numbers_of_function_raises_validation_if_list_has_negative_number(self):
		list_of_integers = [1, 5, 3, -7, 5, 8, 6]
		self.assertRaises(ValueError, code_leveling.get_all_even_numbers_of, list_of_integers)
	def test_that_the_get_even_numbers_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_all_even_numbers_of, list_of_integers)
	def test_that_the_get_even_numbers_of_function_returns_correct_result(self):
		result = code_leveling.get_all_even_numbers_of([1, 5, 2, 3, 7, 4, 5, 8, 6])
		self.assertEqual(result, [2, 4, 8, 6])

	

class TestExtractWordsOf5CharctersOfFunction(unittest.TestCase):
	def test_that_the_extract_words_of_5_charcters_of_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', 'feyi']
		result = code_leveling.extract_words_of_5_charcters_of(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_extract_words_of_5_charcters_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.extract_words_of_5_charcters_of, "not a list")
	def test_that_the_extract_words_of_5_charcters_of_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.extract_words_of_5_charcters_of, list_of_words)		
	def test_that_the_extract_words_of_5_charcters_of_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.extract_words_of_5_charcters_of, list_of_words)
	def test_that_the_extract_words_of_5_charcters_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.extract_words_of_5_charcters_of, list_of_integers)
	def test_that_the_extract_words_of_5_charcters_of_function_returns_correct_result(self):
		result = code_leveling.extract_words_of_5_charcters_of(['name', 'ayo', 'amaka', 'feyi', 'school'])
		self.assertEqual(result, ['amaka', 'school'])



class TestRemoveTuplesWithNumberLessThan2InFunction(unittest.TestCase):
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_receives_a_list_as_input(self):
		list_of_tuples = [(1, 'c'), (5, 'a'), (2, 'd'), (3, 'e')]
		result = code_leveling.remove_tuples_with_number_less_than_2_in(list_of_tuples)
		self.assertTrue(list_of_tuples, list)
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_raises_a_validation_when_input_is_not_a_list_of_tuple(self):
		self.assertRaises(TypeError, code_leveling.remove_tuples_with_number_less_than_2_in, "not a list")
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_raises_validation_if_input_is_not_a_list_of_tuple(self):
		list_of_tuples = [[1, 3], [2, 3]]
		self.assertRaises(TypeError, code_leveling.remove_tuples_with_number_less_than_2_in, list_of_tuples)		
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_raises_validation_if_tuple_in_list_has_both_element_as_number(self):
		list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 9)]
		self.assertRaises(ValueError, code_leveling.remove_tuples_with_number_less_than_2_in, list_of_tuples)
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_raises_validation_if_tuple_in_list_has_both_element_as_strings(self):
		list_of_tuples = [('a', 'b'), ('c', 'd'), ('e', 'f')]
		self.assertRaises(ValueError, code_leveling.remove_tuples_with_number_less_than_2_in, list_of_tuples)
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_raises_validation_if_input_is_empty(self):
		list_of_tuples = []
		self.assertRaises(ValueError, code_leveling.remove_tuples_with_number_less_than_2_in, list_of_tuples)
	def test_that_the_remove_tuples_with_number_less_than_2_in_function_returns_correct_result(self):
		result = code_leveling.remove_tuples_with_number_less_than_2_in([(1, 'c'), (5, 'a'), (2, 'd'), (3, 'e')])
		self.assertEqual(result, [(5, 'a'), (3, 'e')])


class TestGetNumberDivisibleBy3And5InFunction(unittest.TestCase):
	def test_that_the_get_number_divisible_by_3_and_5_in_function_receives_a_range_as_input(self):
		input = range(0, 5)
		result = code_leveling.get_number_divisible_by_3_and_5_in(input)
		self.assertTrue(input, range)
	def test_that_the_get_number_divisible_by_3_and_5_in_function_raises_a_validation_when_input_is_not_a_range(self):
		input = [5, 6, 7]
		self.assertRaises(TypeError, code_leveling.get_number_divisible_by_3_and_5_in, input)
	def test_that_the_get_number_divisible_by_3_and_5_in_function_raises_validation_if_number_in_range_is_negative(self):
		input = range(-1, -7, -1)
		self.assertRaises(ValueError, code_leveling.get_number_divisible_by_3_and_5_in, input)
	def test_that_the_get_number_divisible_by_3_and_5_in_function_raises_validation_if_input_is_empty(self):
		input = range(0)
		self.assertRaises(ValueError, code_leveling.get_number_divisible_by_3_and_5_in, input)
	def test_that_the_get_number_divisible_by_3_and_5_in_function_returns_correct_result(self):
		result = code_leveling.get_number_divisible_by_3_and_5_in(range(0, 16))
		self.assertEqual(result, [15])
		
		
		
class TestGetAllPalindomesOfFunction(unittest.TestCase):
	def test_that_the_get_all_palindomes_of_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', 'feyi']
		result = code_leveling.get_all_palindomes_of(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_get_all_palindomes_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_all_palindomes_of, "not a list")
	def test_that_the_get_all_palindomes_of_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.get_all_palindomes_of, list_of_words)		
	def test_that_the_get_all_palindomes_of_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.get_all_palindomes_of, list_of_words)
	def test_that_the_get_all_palindomes_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_all_palindomes_of, list_of_integers)
	def test_that_the_get_all_palindomes_of_function_returns_correct_result(self):
		result = code_leveling.get_all_palindomes_of(['name', 'ayo', 'amaka', 'madam', 'school'])
		self.assertEqual(result, ['madam'])
	def test_that_the_get_all_palindomes_of_function_returns_correct_result(self):
		result = code_leveling.get_all_palindomes_of(['name', 'ayo', 'amaka', 'school'])
		self.assertEqual(result, "no palindrome found")



class TestGetAllToUpperCaseFunction(unittest.TestCase):
	def test_that_the_get_all_to_uppercase_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', 'feyi']
		result = code_leveling.get_all_to_uppercase(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_get_all_to_uppercase_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_all_to_uppercase, "not a list")
	def test_that_the_get_all_to_uppercase_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.get_all_to_uppercase, list_of_words)		
	def test_that_the_get_all_to_uppercase_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.get_all_to_uppercase, list_of_words)
	def test_that_the_get_all_to_uppercase_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_all_to_uppercase, list_of_integers)
	def test_that_the_get_all_to_uppercase_function_returns_correct_result(self):
		result = code_leveling.get_all_to_uppercase(['name', 'ayo', 'amaka'])
		self.assertEqual(result, ['NAME', 'AYO', 'AMAKA'])

class TestGetEachElementSquareOfFunction(unittest.TestCase):
	def test_that_the_get_each_element_square_of_function_receives_a_range_as_input(self):
		input = range(0, 5)
		result = code_leveling.get_each_element_square_of(input)
		self.assertTrue(input, range)
	def test_that_the_get_each_element_square_of_function_raises_a_validation_when_input_is_not_a_range(self):
		input = [5, 6, 7]
		self.assertRaises(TypeError, code_leveling.get_each_element_square_of, input)	
	def test_that_the_get_each_element_square_of_function_raises_validation_if_number_in_range_has_negative_number(self):
		input = range(-1, -7, -1)
		self.assertRaises(ValueError, code_leveling.get_each_element_square_of, input)
	def test_that_the_get_each_element_square_of_function_raises_validation_if_input_is_empty(self):
		input = range(0)
		self.assertRaises(ValueError, code_leveling.get_each_element_square_of, input)
	def test_that_the_get_each_element_square_of_function_returns_correct_result(self):
		result = code_leveling.get_each_element_square_of(range(1, 4))
		self.assertEqual(result, [1, 4, 9])



class TestCapiltalizeFirstLetterOfFunction(unittest.TestCase):
	def test_that_the_capiltalize_first_letter_of_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', 'feyi']
		result = code_leveling.capiltalize_first_letter_of(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_capiltalize_first_letter_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.capiltalize_first_letter_of, "not a list")
	def test_that_the_capiltalize_first_letter_of_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.capiltalize_first_letter_of, list_of_words)		
	def test_that_the_capiltalize_first_letter_of_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.capiltalize_first_letter_of, list_of_words)
	def test_that_the_capiltalize_first_letter_of_function_raises_validation_if_input_is_empty(self):
		list_of_words = []
		self.assertRaises(ValueError, code_leveling.capiltalize_first_letter_of, list_of_words)
	def test_that_the_capiltalize_first_letter_of_function_returns_correct_result(self):
		result = code_leveling.capiltalize_first_letter_of(['name', 'ayo', 'amaka'])
		self.assertEqual(result, ['Name', 'Ayo', 'Amaka'])


class TestGet10PercentTaxEachOfFunction(unittest.TestCase):
	def test_that_the_get_10_percent_tax_each_of_function_receives_a_list_as_input(self):
		list_of_numbers = [1, 5, 3, 7, 8, 6]
		result = code_leveling.get_10_percent_tax_each_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_10_percent_tax_each_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_10_percent_tax_each_of, "not a list")
	def test_that_the_get_10_percent_tax_each_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = ['awele', 'nutrient', 'plate']
		self.assertRaises(ValueError, code_leveling.get_10_percent_tax_each_of, list_of_integers)		
	def test_that_the_get_10_percent_tax_each_of_function_raises_validation_if_list_has_negative_number(self):
		list_of_integers = [1, 5, 3, -7, 5, 8, 6]
		self.assertRaises(ValueError, code_leveling.get_10_percent_tax_each_of, list_of_integers)
	def test_that_the_get_10_percent_tax_each_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_10_percent_tax_each_of, list_of_integers)
	def test_that_the_get_10_percent_tax_each_of_function_returns_correct_result(self):
		result = code_leveling.get_10_percent_tax_each_of([10, 20, 30, 60])
		self.assertEqual(result, [11, 22, 33, 66])


class TestGetSumOfEachOfFunction(unittest.TestCase):
	def test_that_the_get_sum_of_each_of_function_receives_a_list_as_input(self):
		list_of_numbers = [1, 5, 3, 7, 8, 6]
		result = code_leveling.get_sum_of_each_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_sum_of_each_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_sum_of_each_of, "not a list")
	def test_that_the_get_sum_of_each_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = ['awele', 'nutrient', 'plate']
		self.assertRaises(ValueError, code_leveling.get_sum_of_each_of, list_of_integers)		
	def test_that_the_get_sum_of_each_of_function_raises_validation_if_list_has_negative_number(self):
		list_of_integers = [1, 5, 3, -7, 5, 8, 6]
		self.assertRaises(ValueError, code_leveling.get_sum_of_each_of, list_of_integers)
	def test_that_the_get_sum_of_each_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_sum_of_each_of, list_of_integers)
	def test_that_the_get_sum_of_each_of_function_returns_correct_result(self):
		result = code_leveling.get_sum_of_each_of([10, 20, 30, 60])
		self.assertEqual(result, 120)


class TestGetMaximumElementOfFunction(unittest.TestCase):
	def test_that_the_get_maximum_element_of_function_receives_a_list_as_input(self):
		list_of_numbers = [1, 5, 3, 7, 8, 6]
		result = code_leveling.get_maximum_element_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_maximum_element_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_maximum_element_of, "not a list")
	def test_that_the_get_maximum_element_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = ['awele', 'nutrient', 'plate']
		self.assertRaises(ValueError, code_leveling.get_maximum_element_of, list_of_integers)		
	def test_that_the_get_maximum_element_of_function_raises_validation_if_list_has_negative_number(self):
		list_of_integers = [1, 5, 3, -7, 5, 8, 6]
		self.assertRaises(ValueError, code_leveling.get_maximum_element_of, list_of_integers)
	def test_that_the_get_maximum_element_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_maximum_element_of, list_of_integers)
	def test_that_the_get_maximum_element_of_function_returns_correct_result(self):
		result = code_leveling.get_maximum_element_of([10, 20, 30, 60])
		self.assertEqual(result, 60)


class TestMergeEachElementOfFunction(unittest.TestCase):
	def test_that_the_merge_each_element_of_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', 'feyi']
		result = code_leveling.merge_each_element_of(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_merge_each_element_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.merge_each_element_of, "not a list")
	def test_that_the_merge_each_element_of_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.merge_each_element_of, list_of_words)		
	def test_that_the_merge_each_element_of_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.merge_each_element_of, list_of_words)
	def test_that_the_merge_each_element_of_function_raises_validation_if_input_is_empty(self):
		list_of_words = []
		self.assertRaises(ValueError, code_leveling.merge_each_element_of, list_of_words)
	def test_that_the_merge_each_element_of_function_returns_correct_result(self):
		result = code_leveling.merge_each_element_of(['I', 'love', 'amaka'])
		self.assertEqual(result, 'I love amaka')



class TestGetProductOfSquaresOfEachElementOfFunction(unittest.TestCase):
	def test_that_the_get_product_of_squares_of_each_element_of_function_receives_a_list_as_input(self):
		list_of_numbers = [1, 5, 3, 7, 8, 6]
		result = code_leveling.get_product_of_squares_of_each_element_of(list_of_numbers)
		self.assertTrue(list_of_numbers, list)
	def test_that_the_get_product_of_squares_of_each_element_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_product_of_squares_of_each_element_of, "not a list")
	def test_that_the_get_product_of_squares_of_each_element_of_function_raises_validation_if_input_is_not_a_list_of_numbers(self):
		list_of_integers = ['awele', 'nutrient', 'plate']
		self.assertRaises(ValueError, code_leveling.get_product_of_squares_of_each_element_of, list_of_integers)		
	def test_that_the_get_product_of_squares_of_each_element_of_function_raises_validation_if_list_has_negative_number(self):
		list_of_integers = [1, 5, 3, -7, 5, 8, 6]
		self.assertRaises(ValueError, code_leveling.get_product_of_squares_of_each_element_of, list_of_integers)
	def test_that_the_get_product_of_squares_of_each_element_of_function_raises_validation_if_input_is_empty(self):
		list_of_integers = []
		self.assertRaises(ValueError, code_leveling.get_product_of_squares_of_each_element_of, list_of_integers)
	def test_that_the_get_product_of_squares_of_each_element_off_function_returns_correct_result(self):
		result = code_leveling.get_product_of_squares_of_each_element_of([1, 2, 3, 6])
		self.assertEqual(result, 1296)



class TestGetTheAdditionOfFunction(unittest.TestCase):
	def test_that_the_get_the_addition_of_function_receives_a_list_as_input(self):
		list_of_tuples = [(1, 2), (5, 3), (2, 4), (3, 5)]
		result = code_leveling.get_the_addition_of(list_of_tuples)
		self.assertTrue(list_of_tuples, list)
	def test_that_the_get_the_addition_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_the_addition_of, "not a list")
	def test_that_the_get_the_addition_of_function_raises_validation_if_input_is_not_a_list_of_tuple(self):
		list_of_tuples = [[1, 3], [2, 3]]
		self.assertRaises(TypeError, code_leveling.get_the_addition_of, list_of_tuples)		
	def test_that_the_get_the_addition_of_function_raises_validation_if_tuple_in_list_has_both_letter_and_number(self):
		list_of_tuples = [(1, 2), ('a', 4), (5, 'd'), (7, 'c'), ('b', 9)]
		self.assertRaises(ValueError, code_leveling.get_the_addition_of, list_of_tuples)
	def test_that_the_get_the_addition_of_function_raises_validation_if_tuple_in_list_has_both_element_as_strings(self):
		list_of_tuples = [('a', 'b'), ('c', 'd'), ('e', 'f')]
		self.assertRaises(ValueError, code_leveling.get_the_addition_of, list_of_tuples)
	def test_that_the_get_the_addition_of_function_raises_validation_if_input_is_empty(self):
		list_of_tuples = []
		self.assertRaises(ValueError, code_leveling.get_the_addition_of, list_of_tuples)
	def test_that_the_get_the_addition_of_function_returns_correct_result(self):
		result = code_leveling.get_the_addition_of([(1, 3), (5, 4), (2, 7)])
		self.assertEqual(result, [4, 9, 9])



class TestGetNumericStringsOfFunction(unittest.TestCase):
	def test_that_the_get_numeric_strings_of_function_receives_a_list_as_input(self):
		list_of_words = ['name', 'ayo', 'amaka', '123']
		result = code_leveling.get_numeric_strings_of(list_of_words)
		self.assertTrue(list_of_words, list)
	def test_that_the_get_numeric_strings_of_function_raises_a_validation_when_input_is_not_a_list(self):
		self.assertRaises(TypeError, code_leveling.get_numeric_strings_of, "not a list")
	def test_that_the_get_numeric_strings_of_function_raises_validation_if_input_is_not_a_list_of_words(self):
		list_of_words = [1, 2, 3]
		self.assertRaises(ValueError, code_leveling.get_numeric_strings_of, list_of_words)		
	def test_that_the_get_numeric_strings_of_function_raises_validation_if_list_has_an_element_that_is_number(self):
		list_of_words = [1,'name', 'ayo', 'amaka', 'feyi']
		self.assertRaises(ValueError, code_leveling.get_numeric_strings_of, list_of_words)
	def test_that_the_get_numeric_strings_of_function_raises_validation_if_input_is_empty(self):
		list_of_words = []
		self.assertRaises(ValueError, code_leveling.get_numeric_strings_of, list_of_words)
	def test_that_the_get_numeric_strings_of_function_returns_correct_result(self):
		result = code_leveling.get_numeric_strings_of(['123', '456', 'amaka'])
		self.assertEqual(result, 579)

