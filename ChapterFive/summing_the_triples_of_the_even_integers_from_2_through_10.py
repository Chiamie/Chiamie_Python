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


#map the list of even numbers ny tripling each of them
def triple_each_element_of(x):
	return x ** 3
	
list_of_tripled_integers = list(map(triple_each_element_of, list_of_even_integers))

#get the total of the triple of even numbers from 1 through 10

total_of_the_triples_of_even_numbers = sum(list_of_tripled_integers)
print("The total of the triples of the even integers from 1 through 10 is " + str(total_of_the_triples_of_even_numbers))


#Reimplementing the above code with list comprehension

#using a list comprehension to create a list of integers

		
















