from vector_drawing import *

q = [(1,0), (1,1), (0,1), (0,0)]

t1 = [q[0], q[2], q[1]] # red
t2 = [q[0], q[2], q[3]] # green

draw(
    Points(*q),
    Polygon(*q, color=blue),
    Polygon(*t1, color=red),
    Polygon(*t2, color=green),
)
