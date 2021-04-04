from helpers import *


def derivative(function, time, digits=6):
    tolerance = 10 ** (-digits)
    h = 1
    approx = avarage(function, time, time + h)
    for i in range(2 * digits):
        h = h / 10
        next_approx = avarage(function, time, time + h)
        if (approx - next_approx) < tolerance:
            return next_approx
        else:
            approx = next_approx

    raise Exception("Did not converge")


plot_function(lambda t: derivative(volume, t), 0, 10)
plot_show()
