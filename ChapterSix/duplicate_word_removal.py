#6.6 (Duplicate Word Removal)

def display_unique_words_in_alpha_order(list_of_words):
	unique_words = set()
	for word in list_of_words:
		word = word.lower()
		unique_words.add(word)
	return sorted(unique_words)
	

student_names = ['feyi', 'leo', 'James', 'Sarah', 'sarah',  'Achalugo', 'obi', 'James', ]
print(display_unique_words_in_alpha_order(student_names))





