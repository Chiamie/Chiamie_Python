#3.22  (Optional else Clause of a Loop) 

for i in range(5):
	value = int(input('Enter an integer (-1 to break): '))
	print('You entered:', value)
	if value == -1:
		break
else:
	print('The loop terminated without executing the break')
	
	
	
#the else clause in loops is used when you want some actions to be performed when a loop completes normally without being terminated prematurely.
#the else is not inside the loop
#the if statement is in the loop, and the break is inside the if which inside the for.
#for the above the loop iterates 5 times from 0 to 4, so it would be prompted to enter an integer 5 times.
#if each of the prompts gets a value that is not -1 for each of the prompts, the loop will move to the else statement.
#However if -1 is entered in any of the prompts, the loop terminates prematurely and the else statement will not execute.