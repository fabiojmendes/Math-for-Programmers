from math import sqrt, pi
from vector_drawing import *


def add(*vectors):
    return (sum(v[0] for v in vectors),
            sum(v[1] for v in vectors))


def translate(trlt, vectors):
    return [add(trlt, v) for v in vectors]


def length(v):
    return sqrt(v[0]**2 + v[1]**2)


def scale(v, s):
    return (v[0] * s, v[1] * s)


dino_vectors = [
    (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
    (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
]

# dinos = [Polygon(*translate((i * 12, j * 12), dino_vectors))
#          for i in range(0, 10) for j in range(0, 10)]

print("Max lentgh is:", max(dino_vectors, key=length))

# for i in range(0, 10):
#     for j in range(0, 10):
#         vecs = translate((i * 12, j * 12), dino_vectors)
#         dinos.append(Polygon(*vecs))

v = (sqrt(2), sqrt(3))
vpi = scale(v, pi)

draw(
    # Points(*dino_vectors),
    # Polygon(*dino_vectors),
    # *dinos,
    Points(v, vpi),
    Segment((0, 0), vpi, color=red),
    Segment((0, 0), v),
)
