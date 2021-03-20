from draw2d import *
from vectors import *

o = (0, 0)
v1 = (1, 4)
v2 = (4, 1)

v2comp = dot(v1, v2) / length(v2)
v1_proj_v2 = scale(v2comp, unit(v2))

print(v1_proj_v2)

draw2d(
    Arrow2D(v1, color=red),
    Arrow2D(v2, color=blue),
    Arrow2D(v1_proj_v2, color=purple),
    Segment2D(v1, v1_proj_v2, color=gray),
)
