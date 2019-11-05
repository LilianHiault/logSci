import numpy as np
import matplotlib.pyplot as plt


# Functions


# Main
x = np.linspace(-10, 10, 1000)
y = np.sin(x) / x
plt.plot(x, y)
# plt.axis("equal")

plt.figure()
x = np.linspace(0, 20, 1000)
y = np.sin(x**2)
plt.plot(x, y)
# plt.axis("equal")

plt.show()
