from transforms import *

A = (
    (1.3, -0.7),
    (6.5, 3.2),
)

v = (-2.5, 0.3)


u = multiply_matrix_vector(A, v)

print(u)
