import numpy as np
import matplotlib.pyplot as plt


# Functions
def f(x):
    return (1 / x)


def fp(x):
    return (- 1 / x**2)


# Main
x0 = eval(input("Tangente au point x0 = "))
x = np.linspace(1, 3, 400)
tan = fp(x0) * (x - x0) + f(x0)
plt.plot(x, tan, label="tan")
plt.plot(x, f(x), label="f(x)")
plt.axis("equal")
plt.legend(loc=0)
plt.xlim(1, 3)
plt.title("Tangente de f au point %d" % (x0))
plt.show()
