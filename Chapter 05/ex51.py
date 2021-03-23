from math import pi
from transforms import *
from draw3d import *


def infer_matrix(n, transformation):
    matrix = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        matrix.append(transformation(row))
    return tuple(matrix)


if __name__ == '__main__':
    v = (1, 1, 1)
    # m = infer_matrix(3, rotate_x_by(3/2 * pi))
    m = infer_matrix(3, rotate_z_by(pi/2))
    # m = infer_matrix(3, scale_by(2))
    print(m)

    tv = multiply_matrix_vector(m, v)
    print(tv)

    draw3d(Arrow3D(v), Arrow3D(tv, color=blue))
