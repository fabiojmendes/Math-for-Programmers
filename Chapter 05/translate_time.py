from teapot import load_triangles
from draw_model import draw_model


def to_4d_vector(v):
    return (*v, 1)


def translate_matrix(t):
    time = t/10000
    return (
        (1, 0, 0, min(2, 2 * time)),
        (0, 1, 0, min(2, 2 * time)),
        (0, 0, 1, max(-3, -3 * time)),
        (0, 0, 0, 1),
    )


teapot = [(to_4d_vector(t[0]),
           to_4d_vector(t[1]),
           to_4d_vector(t[2])) for t in load_triangles()]


draw_model(teapot, get_matrix=translate_matrix)
