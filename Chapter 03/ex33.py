from vectors import *
from draw3d import *

o = (0, 0, 0)
v = (4, 0, 3)
u = (-1, 0, 1)
a = add(u, v)

print("u v a", u, v, a)

draw3d(
    # Segment3D(o, u, color=green),
    # Segment3D(u, add(u, v), color=red),
    Arrow3D(tip=u, color=blue),
    Arrow3D(tail=u, tip=a, color=red),

    Arrow3D(tip=v, color=red),
    Arrow3D(tail=v, tip=a, color=blue),

    Arrow3D(tip=a, color=purple),
)
