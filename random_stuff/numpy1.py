import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(type(a))
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.shape)

b = np.array([3.1, 21, 23.23, 3.4, 6.2])
print(type(b))
print(b.dtype)

c = np.array([20, 1, 2, 3, 4])
c[0] = 100

#adding 2 vectors

u = [0, 1]
v = [1, 0]
z = []
for n, m in zip(u,v):
	z.append(n + m)
print(z)

#adding 2 vectors using numpy

x = np.array([0, 1])
y = np.array([1, 0])
w = x + y
print(w)
dot = np.dot(x,y)
print(dot)

print(np.pi)

q = np.array([0, np.pi/2, np.pi])
e = np.sin(q)
print(q, e)



print(np.linspace(-2, 2, num = 10))




import numpy as np 
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
print(a)