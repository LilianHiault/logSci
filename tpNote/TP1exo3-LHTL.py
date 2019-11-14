import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


# Lilian HIAULT et Tom LHÔPITAL


# Fonctions
def lignbris(x1, y1, x5, y5):
    p1 = [x1, y1]
    p5 = [x5, y5]
    
    x2 = (2 / 3) * p1[0] + (1 / 3) * p5[0]
    y2 = (2 / 3) * p1[1] + (1 / 3) * p5[1]
    p2 = [x2, y2]
    
    x3 = (1 / 2) * p1[0] + (1 / 2) * p5[0] + (np.sqrt(3) / 6) * p1[1] - (np.sqrt(3) / 6) * p5[1]
    y3 = (1 / 2) * p1[1] + (1 / 2) * p5[1] - (np.sqrt(3) / 6) * p1[0] + (np.sqrt(3) / 6) * p5[0]
    p3 = [x3, y3]
    
    x4 = (1 / 3) * p1[0] + (2 / 3) * p5[0]
    y4 = (1 / 3) * p1[1] + (2 / 3) * p5[1]
    p4 = [x4, y4]
    
    plt.plot([p1[0], p2[0], p3[0], p4[0], p5[0]],[p1[1], p2[1], p3[1], p4[1], p5[1]], color = "b")
    plt.xlim(- 0.1, 1.1)
    plt.ylim(- 0.2, 0.5)
    plt.title("Ligne brisée des points p1 à p5 avec p1 = (%d, %d) et p5 = (%d, %d)" % (x1, y1, x5, y5))
    
def vonkoch(n, x1, y1, x5, y5):
    if n == 1:
        lignbris(x1, y1, x5, y5)
    else:
        vonkoch(n - 1, x1, y1, (2 / 3) * x1 + (1 / 3) * x5, (2 / 3) * y1 + (1 / 3) * y5)
        vonkoch(n - 1, (2 / 3) * x1 + (1 / 3) * x5, (2 / 3) * y1 + (1 / 3) * y5, (1 / 2) * x1 + (1 / 2) * x5 + (np.sqrt(3) / 6) * y1 - (np.sqrt(3) / 6) * y5, (1 / 2) * y1 + (1 / 2) * y5 - (np.sqrt(3) / 6) * x1 + (np.sqrt(3) / 6) * x5)
        vonkoch(n - 1, (1 / 2) * x1 + (1 / 2) * x5 + (np.sqrt(3) / 6) * y1 - (np.sqrt(3) / 6) * y5, (1 / 2) * y1 + (1 / 2) * y5 - (np.sqrt(3) / 6) * x1 + (np.sqrt(3) / 6) * x5, (1 / 3) * x1 + (2 / 3) * x5, (1 / 3) * y1 + (2 / 3) * y5)
        vonkoch(n - 1, (1 / 3) * x1 + (2 / 3) * x5, (1 / 3) * y1 + (2 / 3) * y5, x5, y5)

'''def snowflake(n):
    p1 = [0, 0]
    p2 = [2, 0]
    p3 = [1, 1] 
    x = [p1[0], p2[0], p3[0], p1[0]]
    y = [p1[1], p2[1], p3[1], p1[1]]
    p1 = [(x[0] + x[1]) / 2, (y[0] + y[1]) / 2]
    p2 = [(x[1] + x[2]) / 2, (y[1] + y[2]) / 2]
    p3 = [(x[2] + x[3]) / 2, (y[2] + y[3]) / 2]
    
    plt.plot(x, y)
    plt.title("Triangle")
    plt.show()'''
    # Appliquer vonkoch(n) à chaque segment du triangle

# Main

#lignbris(0, 0, 1, 0)
vonkoch(3, 0, 0, 1, 0)
#snowflake(5)