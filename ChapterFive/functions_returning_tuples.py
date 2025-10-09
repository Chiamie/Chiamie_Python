def rotate(arg1, arg2, arg3):
	return (arg3, arg1, arg2)


a = 'Doug'
b = 22
c = 1984

a, b, c = rotate(a, b, c)
print(a, b, c)
a, b, c = rotate(a, b, c)
print(a, b, c)
a, b, c = rotate(a, b, c)
print(a, b, c)



