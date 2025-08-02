#3.23  (Validating Indentation) 
grade = 93
if grade >= 90:
   print('A')
print('Great Job!')
print('Take a break from studying')


"""When I aligned the second print statement under the i in the if key
word, tabnanny flagged that as an error: IndentationError: expected an indented block after 'if' statement on line 3
if you indent line 4, it is under the if statement, however if you do not indent line 5 and 6 they are not in the if statement.
so the print didnt happen because of the condition being true.



"""