from transforms import multiply_matrix_vector as proof


def multiply_matrix_vector(matrix, vector):
    return tuple(
        sum(col * coord for col, coord in zip(row, vector))
        for row in matrix
    )


if __name__ == "__main__":
    A = (
        (2, 1, 1),
        (1, 2, 1),
        (1, 1, 2),
    )

    v = (2, 3, 4)

    print("Test: ", multiply_matrix_vector(A, v))
    print("Proof:", proof(A, v))
