from math import sqrt, pi, tan, sin, cos
from vector_drawing import *
from random import uniform


def scale(s, v):
    return (v[0] * s, v[1] * s)


def add(*vectors):
    return (sum(v[0] for v in vectors),
            sum(v[1] for v in vectors))


def subtract(va, vb):
    return (va[0]-vb[0], va[1]-vb[1])


def length(v):
    return sqrt(v[0]**2 + v[1]**2)


def distance(v1, v2):
    dis = subtract(v1, v2)
    return length(dis)


def perimeter(vectors):
    p = 0
    distances = [distance(vectors[i], vectors[(i+1) % len(vectors)])
                 for i in range(0, len(vectors))]
    return sum(distances)


def to_cartesian(v):
    l, a = v
    return (l * cos(a), l * sin(a))


polar = [(cos(5*x*pi/500.0), 2*pi*x/1000.0) for x in range(0, 1000)]

points = [to_cartesian(v) for v in polar]

segs = [Segment(points[i], points[(i+1) % len(points)])
        for i in range(0, len(points))]

draw(
    Polygon(*points, color=green),
)
