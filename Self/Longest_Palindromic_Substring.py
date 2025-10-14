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
