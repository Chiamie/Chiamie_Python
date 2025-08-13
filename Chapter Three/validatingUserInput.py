passes = 0
failures = 0
result = int(input("Enter result(1 or 2)"))
while (result != 1 or result != 2):
	if result == 1 or result == 2:
 		passes = passes + 1
 		break; 
	else:
 		failures = failures + 1
 		result = int(input("Enter result(1 or 2)"))
print("passed: ", passes)
print("failed: ", failures)
 		
 	
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 