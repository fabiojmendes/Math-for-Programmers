from draw3d import *
from vectors import *

v1 = (-1, 0, 0)
v2 = (0, -1, 0)
v3 = (0, 0, 1)

points = Points3D(v1, v2, v3)

segs = [Segment3D(v1, v2), Segment3D(v1, v3), Segment3D(v2, v3)]

c = cross(subtract(v2, v1), subtract(v3, v1))

draw3d(
    points,
    *segs,
    Arrow3D(subtract(v2, v1), color=red),
    Arrow3D(subtract(v3, v1), color=purple),
    Arrow3D(c, color=green)
)
