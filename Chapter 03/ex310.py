from vectors import length, scale


def normalize(v):
    l = length(v)
    return scale(1/l, v)
    # return tuple(coord / l for coord in v)

norm = normalize((-1, -1, 2))
print(norm, length(norm))
