#b = [5, 6, 7, 8]
#c = []

#for a_elem, b_elem in zip(a, b):
#	c.append(a_elem + b_elem)
#print(c)

# function example

def add_arrays(x, y):
	z = []
	for x_elem, y_elem in zip(x, y):
		z.append(x_elem + y_elem)
	return z
#print(add_arrays(a, b))

#zipping example

#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#a_zip = zip(list1, list2) 
#zipped_list = list(a_zip) 
#print(zipped_list)