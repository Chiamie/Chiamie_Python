#6.7 (Character Counts)
import re

user_input = input("Enter a sentence")

modified_user_input = re.sub(r'[^\w\s]', '', user_input)

modified_user_input = modified_user_input.lower().split()

print(modified_user_input)
letter_counts = {}
for word in modified_user_input:
	word.split()
	for letter in word:
		if letter in letter_counts:
			letter_counts[letter] +=1
		else:
			letter_counts[letter] = 1

print(letter_counts)





















