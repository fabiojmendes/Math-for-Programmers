from vectors import *

vs = [(x, y) for x in range(-20, 20) for y in range(-20, 20)]

res = [(v1, v2) for v1 in vs for v2 in vs
       if dot(v1, v2) == 21 or dot(v1, v2) == -21]

print(res)
