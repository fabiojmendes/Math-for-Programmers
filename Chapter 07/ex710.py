import matplotlib.pyplot as plt
from vectors import *


def to_standard(u, v):
    x1, y1 = u
    x2, y2 = v
    a = y2 - y1
    b = x1 - x2
    c = x1*y2 - x2*y1
    return (a, b, c)


u = (3, 0)
v = (0, 1)


coords = [add(u, scale(i, v)) for i in range(50)]

xs, ys = zip(*coords)

std = to_standard(u, add(u, v))
print(std)

plt.grid(True)
plt.plot(xs, ys, 'o')
plt.show()
