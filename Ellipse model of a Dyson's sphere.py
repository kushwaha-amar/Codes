import matplotlib.pyplot as plt
import numpy as np

# define the constants
a = 5
b = 4
c = np.sqrt(a*2 - b*2)

# define the x and y values
x = np.linspace(-a, a, 100)
y = b * np.sqrt(1 - (x/a)**2)

# plot the ellipse
plt.plot(x, y, 'b')
plt.plot(x, -y, 'b')
plt.plot([-c, c], [0, 0], 'ro') # foci
plt.plot([0, 0], [-b, b], 'g') # minor axis
plt.plot([-a, a], [0, 0], 'r') # major axis
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse model of a Dyson\'s sphere')
plt.show()