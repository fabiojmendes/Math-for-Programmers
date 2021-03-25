from draw3d import *
from vector_drawing import *
from transforms import *


def to_3d_vector(v):
    return (v[0], v[1], 1)

def to_2d_vector(v):
    return (v[0], v[1])


dino_vectors = [
    (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0),
    (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
]

translate_matrix = (
    (1, 0, 2),
    (0, 1, 2),
    (0, 0, 1),
)

dino3d = [to_3d_vector(v) for v in dino_vectors]

translate_dino = [multiply_matrix_vector(translate_matrix, v) for v in dino3d]

# draw3d(
#     Polygon3D(*dino3d),
#     Polygon3D(*translate_dino, color=red),
# )
draw(
    Polygon(*dino_vectors),
    Polygon(*[to_2d_vector(v) for v in translate_dino], color=red)
)
