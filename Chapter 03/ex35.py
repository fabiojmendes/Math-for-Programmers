from math import sin, cos, pi
from draw3d import *
from vectors import *

vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0, 24)]

arrows = []
running_sum = (0, 0, 0)
for v in vs:
    step = add(running_sum, v)
    arrows.append(Arrow3D(tail=running_sum, tip=step))
    running_sum = step

a = add(*vs)
print(a)

draw3d(*arrows)
