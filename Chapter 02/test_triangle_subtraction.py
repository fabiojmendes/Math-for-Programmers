from vector_drawing import *
from vectors import *

t = [(0, 0), (2, 0), (0, 2)]

o = (0, 0)
v = subtract(t[1], t[0])
u = subtract(t[2], t[0])

draw(
    Points(*t),
    Polygon(*t, color=blue),
    Arrow(u),
    Arrow(v),
)
