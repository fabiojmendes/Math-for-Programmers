from draw3d import *
from vectors import *

o = (0, 0, 0)

r = (1, -1)
v = [(x, y, z) for x in r for y in r for z in r]

edges = [((-1, y, z), (1, y, z)) for y in r for z in r] +\
    [((x, -1, z), (x, 1, z)) for x in r for z in r] +\
    [((x, y, -1), (x, y, 1)) for x in r for y in r]
# segs = []
# for v1 in v:
#     for v2 in v:
#         print(v1, v2, distance(v1, v2))
#         if distance(v1, v2) == 2.0:
#             segs.append(Segment3D(v1, v2))

segs = [Segment3D(v1, v2, color=red)
        for v1 in v for v2 in v if distance(v1, v2) == 2.0]
# segs = filter(lambda s: distance(s.start_point, s.end_point) == 2.0, segs)


print("Segments:", len(edges))
# segs = [Segment3D(v[i], v[(i+1) % len(v)]) for i in range(0, len(v))]

draw3d(
    Points3D(*v, color=blue),
    *[Segment3D(*e) for e in edges],
    *segs,
    # Box3D(*v),
    # Segment3D(o, v),
)
