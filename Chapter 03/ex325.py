from vectors import *
from draw3d import *
from random import randint

u = (0, 0, 1)
vs = [(randint(-5, 5), randint(-5, 5), randint(-5, 5))
      for i in range(10)]

for v in vs:
    print("u:", u, "v:", v, "cross:", cross(u, v))
