import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *


blues = matplotlib.cm.get_cmap('Blues')
degrees_per_sec = 360./5
degrees_per_ms = degrees_per_sec / 1000


def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))


def shade(face, color_map=blues, light=(1, 2, 3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))


def to_triangles(poly):
    if len(poly) == 3:
        yield poly
    elif len(poly) == 4:
        # break down the quad in two triangles
        yield poly[0:3]
        yield poly[0], *poly[2:]
    else:
        raise "Unknown polygon"


light = (1, 2, 3)

faces = [
    ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0)),
    # ((1, 0, 0), (1, 1, 0), (0, 0, 0))
]

triangles = [t for f in faces for t in to_triangles(f)]

for t in triangles:
    print(t)

pygame.init()
display = (400, 400)  # 1
window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # 2

gluPerspective(45, 1, 0.1, 50.0)  # 1
glTranslatef(0.0, 0.0, -5)  # 2
# glFrontFace(GL_CW) # or GL_CCW
glEnable(GL_CULL_FACE)  # 3
glEnable(GL_DEPTH_TEST)  # 4
glCullFace(GL_BACK)  # 5


clock = pygame.time.Clock()  # 1
while True:
    for evt in pygame.event.get():  # 2
        if evt.type == pygame.QUIT or evt.type == KEYDOWN \
                and (evt.key == K_q or evt.key == K_ESCAPE):
            pygame.quit()
            quit()

    millis = clock.tick(60)  # 3
    glRotatef(millis * degrees_per_ms, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for tri in triangles:
        color = shade(tri, blues, light)
        for vertex in tri:
            glColor3fv((color[0], color[1], color[2]))
            glVertex3fv(vertex)
    glEnd()
    pygame.display.flip()
    # print(clock.get_fps())
