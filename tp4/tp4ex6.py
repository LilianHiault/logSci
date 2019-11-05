import numpy as np
import matplotlib.pyplot as plt


# Main
n = eval(input("Ordre n : "))
p1 = [0, 0]
p2 = [2, 0]
p3 = [1, 1]
for i in range(1, n + 1):
    x = [p1[0], p2[0], p3[0], p1[0]]
    y = [p1[1], p2[1], p3[1], p1[1]]
    plt.plot(x, y, label="Ordre %d" % (i))
    p1 = [(x[0] + x[1]) / 2, (y[0] + y[1]) / 2]
    p2 = [(x[1] + x[2]) / 2, (y[1] + y[2]) / 2]
    p3 = [(x[2] + x[3]) / 2, (y[2] + y[3]) / 2]

plt.title("Triangles imbriqués")
# plt.axis("equal")
plt.legend(loc=0)
plt.show()
