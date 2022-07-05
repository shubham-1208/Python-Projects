import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
y =  np.sin(x)*np.sin(x) - np.cos(x)
z = x*x*y
w = np.sin(x)

#%matplotlib inline
plt.plot(x,w,x,y)
plt.xlabel('x values from 0 to 2pi')
plt.ylabel('sin(x) and other f(x)')
plt.title('plot of sin and f(x) from 0 to 2pi')
plt.legend(['sin(x)','f(x)'])
plt.show()