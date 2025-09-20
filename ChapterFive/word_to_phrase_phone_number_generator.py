#5.13 (Word or Phrase to Phone-Number Generator)



def generate_vanity_phone_numbers(string):
	digit_to_letters = [("2", "ABC"), ("3", "DEF"), ("4", "GHI"), ("5", "JKL"), ("6", "MNO"), ("7", "PRS"), ("8", "TUV"), ("9", "WXY")]
	string = string.upper()
	
	if len(string) != 7:
		raise ValueError("string must be 7 characters")
		
	for letter in string:
		if letter == 'Q' or letter == 'Z':
			raise ValueError("string character must not contain Q or Z")
			
	if not string.isalpha():
		raise ValueError("string characters must all be letters")
			
	combinations = [""]
	for character in string:
		new_combination = []
		for combination in combinations:
			for element in digit_to_letters:
				for letter in element[1]:
					if character == letter:
						new_combination.append(combination + element[0])
		combinations = new_combination
	return combination
				



word = "PETCARE"
print(generate_vanity_phone_numbers(word))