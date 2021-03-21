from teapot import load_triangles
from draw_model import draw_model
from transforms import *

triangles = load_triangles()
triangles = polygon_map(scale_by(2), triangles)
triangles = polygon_map(translate_by((-1,0,0)), triangles)

draw_model(triangles)
