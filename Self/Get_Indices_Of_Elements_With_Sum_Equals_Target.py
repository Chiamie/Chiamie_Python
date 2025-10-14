def two_sum(list_of_numbers, target):
	for count in range(0, len(list_of_numbers)):
		for counter in range(1, len(list_of_numbers)):
			if list_of_numbers[count] + list_of_numbers[counter] == target:
				indices = count, counter
				break
	return indices
	
nums = [2,7,11,15]
target = 9	
print(two_sum(nums, target))

nums = [3,3]
target = 6
print(two_sum(nums, target))

nums = [3,2,4]
target = 6
print(two_sum(nums, target))


def two_sum(list_of_numbers, target):
	dict_of_indices = {}
	for index, number in enumerate(list_of_numbers):
		complement = target - number
		if complement in dict_of_indices:
			return [dict_of_indices[complement], index]
		dict_of_indices[number] = index
	return []


