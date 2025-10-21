def is_balanced(string_of_brackets):
	bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
	stack = []
	for char in string_of_brackets:
		if char in bracket_pairs.values():
			stack.append(char)
		elif char in bracket_pairs:
			if not stack or stack[-1] != bracket_pairs[char]:
				return False
			stack.pop()
	return not stack
	

string_of_brackets = "{([<>])}"
print(is_balanced(string_of_brackets))

string_of_brackets = "{{(})}"
print(is_balanced(string_of_brackets))

string_of_brackets = "[]({)"
print(is_balanced(string_of_brackets))
