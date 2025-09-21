#5.23 (Functional-Style Programming: Order of filter and map Calls)


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
number = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
  
print(number)


number = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))
print(number)


[20, 8, 4, 16, 12]
[20, 6, 14, 2, 18, 8, 4, 16, 10, 12]

#For the first one: the filter function executes first. The filter iterates through each of the 
#element of the list and returns it if it is an even number. The list that the filter function will
#return is shorter than the original list.

#Then the map function would collect what the filter function has returned as arguement. The map function 
#multiplies each of the element of its arguement by 2.


#For the second one: the map function is first to execute. It multiplies each of the element of the
#numbers list by 2 then returns the result as a list.
#The length of the list returned by the map function is same as the length of its arguement.

#The filter function then takes the result from the map function as an arguement.
#And check if each of the element is an even number which in this case is True.
#Therefore the result of this filter function is equal in length to the result of the map function.












