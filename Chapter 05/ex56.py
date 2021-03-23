from draw_model import *
from teapot import load_triangles

teapot = load_triangles()


def matrix(t):
    return (
        (2, 1, 1),
        (1, 2, 1),
        (1, 1, 2)
    )


draw_model(teapot, get_matrix=matrix)
