#  Find a 3x3 matrix that rotates a 2D figure in the plane z = 1 by 45°,
# decreases its size by a factor of 2, and translates it by the vector (2, 2).
# Demonstrate that it works by applying it to the vertices of the dinosaur.
from math import pi
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

# rotate_matrix = (
#     (1, 0, 0),
#     (0, 1, 0),
#     (0, 0, 1),
# )
rotate_45_degrees = curry2(rotate2d)(pi/4)
rotation_matrix = infer_matrix(2, rotate_45_degrees)

scale_matrix = (
    (0.5, 0),
    (0, 0.5),
)


# rotation_matrix = infer_matrix(3, rotate_z_by(pi/4))
# translate_matrix = infer_matrix(3, translate_by((2, 2, 0)))
# scale_matrix = infer_matrix(3, scale_by(0.5))

# print("rotation_matrix:", rotation_matrix)
# print("translate_matrix:", translate_matrix)
# print("scale_matrix:", scale_matrix)

matrix = multiply_matrix(scale_matrix, rotation_matrix)
print("scale and rotate:", matrix)

(a, b), (c, d) = matrix
matrix = (
    (a, b, 4),
    (c, d, 4),
    (0, 0, 1),
)
print("scale, rotate and translate:")
for row in matrix:
    print(row)

dino3d = [to_3d_vector(v) for v in dino_vectors]
transformed_dino = [multiply_matrix_vector(matrix, v) for v in dino3d]

# draw3d(
#     Polygon3D(*dino3d),
#     Polygon3D(*translate_dino, color=red),
# )

draw(
    Polygon(*dino_vectors),
    Polygon(*[to_2d_vector(v) for v in transformed_dino], color=red)
)
