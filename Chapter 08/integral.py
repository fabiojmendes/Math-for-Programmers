from helpers import *


def approximate_volume(q, v0, dt, T):
    return v0 + volume_change(q, 0, T, dt)


def approximate_volume_function(q, v0, dt):
    def volume_function(T):
        return approximate_volume(q, v0, dt, T)
    return volume_function


plot_function(approximate_volume_function(flow_rate, 2.3, 0.01), 0, 10)
plot_function(volume, 0, 10)
plot_show()
