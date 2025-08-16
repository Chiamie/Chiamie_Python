#Modified average Function


def average(*args):
	if args is None:
		raise TypeError("average() missing 1 required positional argument.")
	return sum(args) / len(args)
print(average(1, 2, 3, 4, 5, 6))




	
	
	
	
	
	
	
	
	