import numpy
import numpy as np


def PlotCylinderObject(p1, p2, r, nsurfpatches):
    """
    Returns the points needed to generate surface plots for the lateral, upper, and lower faces of the cylinder.

    :param p1: Start point of cylinder [Numpy.Array]
    :param p2: End point of cylinder [Numpy.Array]
    :param r: Radius of cylinder [Float]
    :param nsurfpatches: Number of surface patched for the cylinder [Integer]
    """
    eta1 = np.linspace(0, 1, nsurfpatches)
    eta2 = np.linspace(0, 1, 2)
    [eta1, eta2] = np.meshgrid(eta1, eta2)
    cyl_dir = p2 - p1
    [maxn, maxi] = [np.max(np.absolute())]
    if maxi == 1:
        v1 = []
    elif maxi == 2:
        v1 = []
    elif maxi == 3:
        v1 = []
    else:
        print("what??")

    return None
