from transforms import *


def multiply_matrix(m1, m2):
    return tuple(tuple(dot(row, col) for col in zip(*m2)) for row in m1)


if __name__ == '__main__':
    A = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    )

    B = (
        (-1, -4, -7),
        (-2, -5, -8),
        (-3, -6, -9),
    )

    print(multiply_matrix(A, B))

    C = (
        (0, 1),
        (-1, 0),
    )

    D = (
        (0, -1),
        (1, 0),
    )

    print(multiply_matrix(C, D))
