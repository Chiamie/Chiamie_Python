#5.11 (Summarizing Letters in a String)


def summarize_letters(string):
	result = []
	unique_letters = [item for index, item in enumerate(string) if item not in string[:index]]
	counter = 0
	for count in range(len(string)):
		if unique_letters[count] not in string:
			counter = 1
		else:
			counter += 1
		letter_and_count = unique_letters[count], count
		result.append(letter_and_count)
	return result
	


letter = "I love programming! I hate programming!"
print(summarize_letters(letter))
