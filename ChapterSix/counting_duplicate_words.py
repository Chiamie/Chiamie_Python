#6.5 (Counting Duplicate Words)

text = ('God is not man, man is not God but man is a god.')
text_with_no_punctuation = re.sub(r'[^\w\s]', '', text)
word_counts = {}
for word in text_with_no_punctuation.lower().split():
	if word in word_counts:
		word_counts[word] += 1  
	else:
 		word_counts[word] = 1  
print(f'{"WORD":<12}COUNT')
for word, count in sorted(word_counts.items()):
	print(f'{word:<12}{count}')
print('\nNumber of unique words:', len(word_counts))





