from helpers import *


def line(f, t1, t2):
    a = avarage(f, t1, t2)
    a = avarage(volume, 3, 5)
    return lambda x: avarage(f)
    # return avarage(volume, x, x+0.0001)

def secant_line(f,x1,x2):
    def line(x):
        return f(x1) + (x-x1) * avarage(f, x1, x2)
    return line


plot_functions([volume, secant_line(volume, 6, 8)], 0, 10)
