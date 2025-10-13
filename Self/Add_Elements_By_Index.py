def add_elements_via_index(list_of_numbers1, list_of_numbers2):
	to_string_of_list_of_numbers1 = "".join([str(items) for items in list_of_numbers1])
	to_string_of_list_of_numbers2 = "".join([str(items) for items in list_of_numbers2])
	
	sum_of_numbers = int(to_string_of_list_of_numbers1) + int(to_string_of_list_of_numbers2)
	string_representation_of_sum_of_numbers = str(sum_of_numbers)
	list_of_sum_digits = []
	for count in range(len(string_representation_of_sum_of_numbers) - 1, -1, -1):
		list_of_sum_digits.append(int(string_representation_of_sum_of_numbers[count]))
	return list_of_sum_digits
		
		
l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(add_elements_via_index(l1, l2))
			
			
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]			
print(add_elements_via_index(l1, l2))
			
			
			