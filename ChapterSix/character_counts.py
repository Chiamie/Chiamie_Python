#6.7 (Character Counts)
import re

letter_counts = {}

def get_letter_counts(list_of_words):
	for word in modified_user_input:
		word.split()
		for letter in word:
			if letter in letter_counts:
				letter_counts[letter] +=1
			else:
				letter_counts[letter] = 1
	return letter_counts


user_input = input("Enter a sentence")

modified_user_input = re.sub(r'[^\w\s]', '', user_input)

modified_user_input = modified_user_input.lower().split()

letter_counts = get_letter_counts(modified_user_input)

print("LETTER\tCOUNT")
for key, value in sorted(letter_counts.items()):
	print(f'{key}:\t{value}')


#Challenge: Use a set operation to determine which letters of the alphabet were not in the original string.
import string
letters = set(string.ascii_lowercase)
user_input = set(user_input.lower())
print(letters - user_input) 
















