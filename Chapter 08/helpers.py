import matplotlib.pyplot as plt
import numpy as np

def plot_show():
    plt.show()


def plot_functions(functions, tmin, tmax, tlabel=None, xlabel=None, axes=False, **kwargs):
    ts = np.linspace(tmin, tmax, 1000)
    if tlabel:
        plt.xlabel(tlabel, fontsize=18)
    if xlabel:
        plt.ylabel(xlabel, fontsize=18)
    for f in functions:
        plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax-tmin
        plt.plot([tmin-total_t/10, tmax+total_t/10],
                 [0, 0], c='k', linewidth=1)
        plt.xlim(tmin-total_t/10, tmax+total_t/10)
        xmin, xmax = plt.ylim()
        plt.plot([0, 0], [xmin, xmax], c='k', linewidth=1)
        plt.ylim(xmin, xmax)


def plot_function(f, tmin, tmax, tlabel=None, xlabel=None, axes=False, **kwargs):
    plot_functions([f], tmin, tmax, tlabel, xlabel, axes, **kwargs)


def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)",
                  xlabel="volume (bbl)", axes=axes, **kwargs)


def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)",
                  xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)


def volume(t):
    return (t-4)**3 / 64 + 3.3


def flow_rate(t):
    return 3*(t-4)**2 / 64


def avarage(f, t1, t2):
    return (f(t2) - f(t1)) / (t2 - t1)


def small_volume_change(q, t, dt):
    return q(t) * dt


def volume_change(q, t1, t2, dt):
    return sum(small_volume_change(q, t, dt)
               for t in np.arange(t1, t2, dt))
