pi = 0
maths_symbol = 1
print("Term\tpi approximation")
for term in range(1, 1001):
	divisor = (2 * term) - 1
	pi += maths_symbol  * (4 / divisor)
	maths_symbol *= -1
	print(f"{term: < 5} {pi: <10.5f}")
if round(pi, 3) == 3.142:
	print(term)
elif round(pi, 2) == 3.14:
	print(term)
elif round(pi, 4) == 3.1415:
	print(term)

		
