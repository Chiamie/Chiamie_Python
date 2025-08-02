#3.19 (Brute-Force Computing: Pythagorean Triples)
for adjacents in range(1, 20):
	for opposites in range(adjacents, 20):
		for hypothenuse in range(opposites, 20):
			if adjacents ** 2 + opposites ** 2 == hypothenuse ** 2:
				print(adjacents, opposites, hypothenuse)
		 
