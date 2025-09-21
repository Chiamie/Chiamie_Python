#5.18 (Summing the Triples of the Even Integers from 2 through 10)

def creating_a_list():
	list_of_integers = []
	for number in range(1, 11):
		list_of_integers.append(number)
	return list_of_integers
	

list_of_integers = creating_a_list()

#filter the list to get even numbers
def get_even_numbers_of(x):
	return x % 2 == 0
	
list_of_even_integers = list(filter(get_even_numbers_of, list_of_integers))


		
















