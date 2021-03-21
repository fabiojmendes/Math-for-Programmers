from math import pi
from teapot import load_triangles
from draw_model import draw_model
from transforms import *

triangles = load_triangles()

f = compose(rotate_x_by(pi/2), rotate_z_by(pi/2))
triangles = polygon_map(f, triangles)


draw_model(triangles)
