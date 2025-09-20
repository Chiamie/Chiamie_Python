#5.14 (Is a Sequence Sorted?)
 
def is_ordered(string):
	if sorted(string) != string:
		return False
	return True
	
list_of_ages = [34, 12, 20, 8]
print(is_ordered(list_of_ages))

list_of_ages = [8, 12, 20, 34]
print(is_ordered(list_of_ages))
 
tuple_of_scores = (34, 12, 20, 8)
print(is_ordered(tuple_of_scores))
 
tuple_of_scores = (8, 12, 20, 34)
print(is_ordered(tuple_of_scores))

names = "leo, dozie, chiamaka, adaeze, nneka"
print(is_ordered(names))
 
 
 