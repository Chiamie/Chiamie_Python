#6.8 (Challenge: Writing the Word Equivalent of a Check Amount)


def number_to_words(number):
	number_to_word = {
	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
	5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
	11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
	15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
	20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
	60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
	}
	if number < 20 or number % 10 == 0:
		return number_to_word.get(number, '')
	else:
		tens = (number // 10) * 10
		ones = number % 10
		tens_in_words = number_to_word.get(tens, '')
		ones_in_words = number_to_word.get(ones, '')
		
		return tens_in_words + '-' + ones_in_words
        


number = 56
print(number_to_words(number))
print(number_to_words(99))
print(number_to_words(67))
print(number_to_words(30))



