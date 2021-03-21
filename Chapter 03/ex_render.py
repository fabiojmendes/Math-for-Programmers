from vectors import *
from draw2d import *
import draw3d as d3d

X_AXIS = (1, 0, 0)
Y_AXIS = (0, 1, 0)

X_COORD = 0
Y_COORD = 1
Z_COORD = 2


def component(v, direction):
    return dot(v, direction) / length(direction)


def vector_to_2d(v):
    return (component(v, X_AXIS), component(v, Y_AXIS))


def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]


def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))


def render(faces, light=(1, 2, 3), color="Blues", lines=None):
    color_map = matplotlib.cm.get_cmap(color)
    polygons = []
    for face in faces:
        unormal = unit(normal(face))
        if unormal[Z_COORD] > 0:
            c = color_map(1 - dot(unit(normal(face)), unit(light)))
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            polygons.append(p)

    draw2d(*polygons, axes=False, origin=False, grid=None)


octahedron = [
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
    [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
    [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, 0, 1), (0, 1, 0)],
    [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
]

# d3d.draw3d(
#     *[d3d.Polygon3D(*f) for f in octahedron],
#     d3d.Points3D((1, 2, 3)),
# )

render(octahedron, lines=black)
