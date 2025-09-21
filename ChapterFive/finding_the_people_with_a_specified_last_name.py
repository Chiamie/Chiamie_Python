#5.19 (Finding the People with a Specified Last Name)

list_of_first_and_last_names = [('Mathew', 'jones'), ('Chiamaka', 'Okechukwu'), ('Ada', 'Anyanwu'), ('Loveth', 'Agu'), ('Dozie', 'Jones'), ('Silver', 'Joseph'), ('Leo', 'Micheal'), ('Chinelo', 'Jones'), ('Festus', 'Westlife')]	

def extract_tuple_with_Jones(x):
	return x if x[1].lower() == 'jones' else None
	
people_with_Jones_as_last_name = list(filter(extract_tuple_with_Jones, list_of_first_and_last_names))

print(people_with_Jones_as_last_name)





