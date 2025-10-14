def sum_of_element_at_same_index(list1, list2):
	list3 = []
	for number, value in zip(list1, list2):
		list3.append(number + value)
	return list3
	
list1 = [1, 2, 3] 
list2 = [4, 5, 6]
print(sum_of_element_at_same_index(list1, list2))













