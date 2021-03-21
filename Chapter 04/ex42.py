from teapot import load_triangles
from draw_model import draw_model
from transforms import *

triangles = load_triangles()
triangles = polygon_map(translate_by((0, 0, -5)), triangles)

draw_model(triangles)
