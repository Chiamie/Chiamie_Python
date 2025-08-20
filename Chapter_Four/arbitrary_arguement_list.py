# 4.13 (Arbitrary Argument List)
def product_of(*args):
	result = 1
	for value in args:
		result *= value
	return result
	
print(product_of(5, 10, 15, 20))