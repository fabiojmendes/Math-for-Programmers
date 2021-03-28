import matplotlib.pyplot as plt
import numpy as np

from vectors import *
from vector_drawing import *


def standard_form(u, v):
    x1, y1 = u
    x2, y2 = v
    a = y2 - y1
    b = x1 - x2
    c = x1*y2 - x2*y1
    return (a, b, c)


def intersection(s1, s2):
    a1, b1, c1 = standard_form(*s1)
    a2, b2, c2 = standard_form(*s2)
    matrix = np.array(((a1, b1), (a2, b2)))
    result = np.array((c1, c2))
    return np.linalg.solve(matrix, result)


def segments_intersect(s1, s2):
    u1, u2 = s1
    v1, v2 = s2
    l1, l2 = distance(*s1), distance(*s2)
    try:
        x, y = intersection(s1, s2)
        return (distance(u1, (x, y)) <= l1 and
                distance(u2, (x, y)) <= l1 and
                distance(v1, (x, y)) <= l2 and
                distance(v2, (x, y)) <= l2)
    except np.linalg.linalg.LinAlgError:
        return False


laser = [
    (8, 2.66666667),
    (0, 0),
]

asteroid = [
    (2, 3),
    (4, 2),
    (6, 2),
    (7, 4),
    (6, 6),
    (4, 6),
    (2, 7),
    (1, 5),
]

segments = [(asteroid[i], asteroid[(i+1) % len(asteroid)])
            for i in range(len(asteroid))]

intersections = [seg for seg in segments if segments_intersect(laser, seg)]


# print("Asteroid segments", segments)

print("Intersections", intersections)

draw(
    Arrow(*laser, color=red),
    Points(*asteroid),
    Polygon(*asteroid, color=green, fill=green),
    *[Segment(*seg, color=red) for seg in intersections],
)
