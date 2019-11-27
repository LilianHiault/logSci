import numpy as np
import matplotlib.pyplot as plt

# Main
t = np.linspace(0, 2 * np.pi, 400)
plt.plot(np.cos(t), np.sin(t), label="cercle")
x = [1, -1 / 2, -1 / 2, 1]
y = [0, 3**(1 / 2) / 2, - 3**(1 / 2) / 2, 0]
plt.plot(x, y, label="triangle")
plt.legend(loc=0)
plt.title("Courbes paramétriques")
plt.axis("equal")
plt.show()
