def get_all_sub_string(group_of_characters):
	list_of_sub_string = []
	for count in range(0, len(group_of_characters)):
		sub_string = ""
		for counter in range(count, len(group_of_characters)):
			sub_string += group_of_characters[counter]
			list_of_sub_string.append(sub_string)
	return list_of_sub_string	


def get_all_palindromic_strings(list_of_sub_string):
	list_of_palindromic_strings = []
	for element in list_of_sub_string:
		if element[::-1] == element:
			list_of_palindromic_strings.append(element)
	return list_of_palindromic_strings

def get_longest_palindromic_string(list_of_palindromic_strings):
	largest = ""
	for element in list_of_palindromic_strings:
		if len(element) > len(largest):
			largest = element
	return largest
	
group_of_characters = "babad"
list_of_sub_string = get_all_sub_string(group_of_characters)
list_of_palindromic_strings = get_all_palindromic_strings(list_of_sub_string)
print(get_longest_palindromic_string(list_of_palindromic_strings))