from vectors import *
from math import pi


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0

    def transformed(self):
        rotated = [rotate2d(self.rotation_angle, v) for v in self.points]
        return translate((self.x, self.y), rotated)


if __name__ == "__main__":
    poly = PolygonModel([(0, 1), (-0.5, 0), (0.5, 0)])
    poly.x, poly.y = (5, 5)
    poly.rotation_angle = pi/2
    print(poly.transformed())
