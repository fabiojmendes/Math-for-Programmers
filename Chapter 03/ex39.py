from vectors import *

r = range(1, 100)

o = (0, 0, 0)

vs = [(x, y, z) for x in r for y in r for z in r]

# print(vs)

for v in vs:
    d = distance(o, v)
    if d.is_integer():
        print("Found result:", v, d)
        # break
