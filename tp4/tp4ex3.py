import numpy as np
import matplotlib.pyplot as plt

# Main
x = np.linspace(0, 1, 100)
comp = 0
for t in np.arange(0.4, 3, 0.01):
    y = x**t
    plt.plot(x, y, color=plt.cm.winter(comp))  # , label="t = %f" % (t))
    # plt.legend(loc=0)
    plt.xlim(0, 1)
    plt.title("x puissance t")
    comp += 1
plt.show()
