from vectors import dot


def multiply_matrix_vector(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


if __name__ == "__main__":
    A = (
        (2, 1, 1),
        (1, 2, 1),
        (1, 1, 2),
    )

    v = (2, 3, 4)

    print("Test: ", multiply_matrix_vector(A, v))
