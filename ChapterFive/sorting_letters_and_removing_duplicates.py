#5.16 (Sorting Letters and Removing Duplicates)
import random

letters_of_interest = ['a', 'b', 'c', 'd', 'e', 'f']





def create_a_list_random_letters():
	list_of_letters = []
	for number in range(20):
		random_uppercase_letter = random.choice(letters_of_interest)
		list_of_letters.insert(number, random_uppercase_letter)
	return list_of_letters
	
list_of_letters =create_a_list_random_letters()
print(list_of_letters)

print(sorted(list_of_letters))

print(sorted(list_of_letters, reverse = True))


unique_values = [item for index, item in enumerate(list_of_letters) if item not in list_of_letters[:index]]
print(sorted(unique_values))




