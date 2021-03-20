from draw_model import *
from math import pi
from transforms import *


def load_file(filename):
    lines = None
    v_list = []
    f_list = []
    with open(filename) as file:
        assert(file.readline().rstrip() == 'OFF')
        vertices, faces, edges = map(int, file.readline().split())
        for i in range(vertices):
            vertex = tuple(map(float, file.readline().split()))
            # scale_by(2)
            vertex = (scale_by(2)(rotate_x_by(-pi/2)
                                  (translate_by((-0.5, 0, -0.6))(vertex))))
            v_list.append(vertex)

        for i in range(faces):
            face = list(map(int, file.readline().split()[1:]))
            f_list.append(face)

    return (v_list, f_list)


def to_triangles(poly):
    if len(poly) == 3:
        yield poly
    elif len(poly) == 4:
        # break down the quad in two triangles
        # 0, 1, 2
        # 0, 2, 3
        yield poly[0:3]
        yield [poly[0], poly[2], poly[3]]
    else:
        raise "Unknown polygon"


def load_triangles(vertices, faces):
    triangles = []
    for face in faces:
        poly = [vertices[i] for i in face]
        for t in to_triangles(poly):
            triangles.append(t)

    return triangles


if __name__ == "__main__":
    vertices, faces = load_file("teapot.off")
    triangles = load_triangles(vertices, faces)

    draw_model(triangles)
