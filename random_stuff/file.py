a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = []

#for a_elem, b_elem in zip(a, b):
#	c.append(a_elem + b_elem)
#print(c)


def add_arrays(x, y):
	z = []
	for x_elem, y_elem in zip(x, y):
		z.append(x_elem + y_elem)
	return z
print(add_arrays(a, b))
