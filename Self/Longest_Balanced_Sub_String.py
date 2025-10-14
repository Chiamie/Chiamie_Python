def get_all_sub_string(group_of_characters):
	list_of_sub_string = []
	for count in range(0, len(group_of_characters)):
		sub_string = ""
		for counter in range(count, len(group_of_characters)):
			sub_string += group_of_characters[counter]
			list_of_sub_string.append(sub_string)
	return list_of_sub_string	
	
def get_all_balanced_sub_string(list_of_sub_string):
	balanced_sub_strings_count = {}
	for index in range(0, len(list_of_sub_string)):
		count_of_characters = iterate_through_a_list(list_of_sub_string, index)
		if is_values_equal(count_of_characters):
			balanced_sub_strings_count[list_of_sub_string[index]] = count_of_characters
	return balanced_sub_strings_count
		
def iterate_through_a_list(list_of_sub_string, index):
	count_of_characters = {}
	for count in range(0, len(list_of_sub_string[index])):
		key = list_of_sub_string[index][count]
		if key in count_of_characters:
			count_of_characters[key] += 1
		else:
			count_of_characters[key] = 1
	return count_of_characters

def is_values_equal(count_of_characters):
	value_set = set(count_of_characters.values())
	return len(value_set) == 1
		
def get_longest_sub_string(balanced_sub_strings_count):
	largest = ""
	for key in balanced_sub_strings_count:
		if len(key) > len(largest):
			largest = key
	return len(largest)
	
#def get_longest_sub_string(balanced_sub_strings_count):
#    return max(balanced_sub_strings_count, key=len)

group_of_characters = "zzabccy"
list_of_sub_string = get_all_sub_string(group_of_characters)
balanced_sub_strings_count = get_all_balanced_sub_string(list_of_sub_string)
print(get_longest_sub_string(balanced_sub_strings_count))
	

group_of_characters = "aba"
list_of_sub_string = get_all_sub_string(group_of_characters)
balanced_sub_strings_count = get_all_balanced_sub_string(list_of_sub_string)
print(get_longest_sub_string(balanced_sub_strings_count))
	
	
group_of_characters = "abbac"
list_of_sub_string = get_all_sub_string(group_of_characters)
balanced_sub_strings_count = get_all_balanced_sub_string(list_of_sub_string)
print(get_longest_sub_string(balanced_sub_strings_count))
	

group_of_characters = "aabcc"
list_of_sub_string = get_all_sub_string(group_of_characters)
balanced_sub_strings_count = get_all_balanced_sub_string(list_of_sub_string)
print(get_longest_sub_string(balanced_sub_strings_count))
	
	
	
	
	
	