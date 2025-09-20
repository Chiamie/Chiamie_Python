def number_word_generator(phone_number):
	digit_to_letters = [("2", "ABC"), ("3", "DEF"), ("4", "GHI"), ("5", "JKL"), ("6", "MNO"), ("7", "PRS"), ("8", "TUV"), ("9", "WXY")]
	phone_number = phone_number.replace("-", "")

	if len(phone_number) != 7:
		raise ValueError("Number must be 7 digits long")

	for digit in phone_number:
		valid = False
		for element in digit_to_letters:
			if digit == element[0]:
				valid = True
				break
		if not valid:
			raise ValueError("Number cannot contain 0 or 1")

	combinations = [""]
	for digit in phone_number:
		new_combination = []
		for combination in combinations:
			for element in digit_to_letters:
				if element[0] == digit:
					for letter in element[1]:
						new_combination.append(combination + letter)
		combinations = new_combination
	return combinations
				

seven_digit_number = "432-9586"
print(number_word_generator(seven_digit_number))
length = number_word_generator(seven_digit_number)
print("This phone number can derive " + str(len(length)) + " combinations")