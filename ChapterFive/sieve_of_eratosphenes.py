# 5.8 (Sieve of Eratosthenes) 


list_primes = [True] * 1000

count = 2
for index in range(2, 1000):
	if index in [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31]:
		if list_primes[index] == True:
			for count in range(index + 1, 1000):
				if count % index == 0:
					list_primes[count] = False
	

print(list_primes)















