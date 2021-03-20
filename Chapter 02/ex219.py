from math import sqrt, pi, atan2, sin, cos, radians
from vector_drawing import *
from random import uniform


def scale(s, v):
    return (v[0] * s, v[1] * s)


def add(*vectors):
    return (sum(v[0] for v in vectors),
            sum(v[1] for v in vectors))


def subtract(va, vb):
    return (va[0]-vb[0], va[1]-vb[1])


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


def rotate(angle, vectors):
    polar = [to_polar(v) for v in vectors]
    rot = [(l, angle + a) for l, a in polar]
    return [to_cartesian(r) for r in rot]


def to_polar(vector):
    x, y = vector
    return (length(vector), atan2(y, x))


def to_cartesian(vector):
    l, a = vector
    return (cos(a) * l, sin(a) * l)


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
    # prev = None
    # for v in vectors:
    #     if prev is not None:
    #         p += distance(prev, v)
    #     prev = v

    # p += distance(prev, vectors[0])
    # return p


def random_r():
    return uniform(-3, 3)


def random_s():
    return uniform(-1, 1)


dino_vectors = [
    (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
    (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
]

rot_dino = translate((8, 8), rotate(5 * pi/3, dino_vectors))


draw(
    Polygon(*dino_vectors),
    Polygon(*rot_dino, color=red),
)
