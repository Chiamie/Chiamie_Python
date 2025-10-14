def generate_range_for_node(integer):
	values_for_node = []
	for number in range(1, integer):
		values_for_node.append(number)
	return values_for_node

def generate_ancestors_of_nodes(values_for_node, edges):
	ancestors = []
	list_of_added_nodes = {}
	for number in values_for_node:
		print(number)
		for count in range(0, len(edges)):
			if edges[count][1] == number:
				print(edges[count][1])
				if edges[count][0] in list_of_added_nodes:
					ancestors.append((edges[count][0], list_of_added_nodes[edges[count][0]]))
					print("here you have", ancestors)
				else:
					ancestors.append(edges[count][0])
					print("this is ", ancestors)
					list_of_added_nodes[edges[count][1]] = edges[count][0]
	return ancestors

def get_number_of_perfect_square_ancestors(values_for_node, ancestors, list_of_numbers):
		sum_of_all_values_for_nodes = 0
		for element_in_values_for_node, element_in_ancestors in zip(values_for_node, ancestors):
			print("acha", element_in_values_for_node, element_in_ancestors)
			if type(element_in_ancestors) == tuple:
				for element in element_in_ancestors:
					if (list_of_numbers[element_in_values_for_node] * list_of_numbers[element]) ** 0.5 % 1 == 0:
						sum_of_all_values_for_nodes += 1
			else:
				if (list_of_numbers[element_in_values_for_node] * list_of_numbers[element_in_ancestors]) ** 0.5 % 1 == 0:
					sum_of_all_values_for_nodes += 1
		return sum_of_all_values_for_nodes
				


integer = 3
values_for_node = generate_range_for_node(integer)
edges = [[0, 1], [1,2]]
ancestors = generate_ancestors_of_nodes(values_for_node, edges)
print(ancestors)

list_of_numbers = [2,8,2]
print(get_number_of_perfect_square_ancestors(values_for_node, ancestors, list_of_numbers))
		


