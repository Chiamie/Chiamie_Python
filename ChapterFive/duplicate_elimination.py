def get_unique_values_of(list_of_values):
	list_of_values = sorted(list_of_values)
	unique_values = [item for index,  item in enumerate(list_of_values) if item not in list_of_values[:index]]
	return unique_values


ages = [56, 12, 90, 34, 89, 12, 34, 56, 12]
print(get_unique_values_of(ages))