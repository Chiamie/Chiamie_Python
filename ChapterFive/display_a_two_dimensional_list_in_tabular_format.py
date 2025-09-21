#5.20 (Display a Two-Dimensional List in Tabular Format)


def display_table(two_dimensional_list):
	for index in range(len(two_dimensional_list[0])):
		print(f"\t{index}", end="")
	for index in range(len(two_dimensional_list)):
		print('\n')
		print(f"{index}\t", end="")
		for element in two_dimensional_list[index]:
			print(f"{element}\t", end="")              

ages = [[56, 57, 58], [59, 60, 61], [62, 63, 64]]
display_table(ages)


 

