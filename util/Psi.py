import numba
import numpy as np
@numba.jit
def Psi(a):
    # convexn   0
    return np.sqrt(a)

    # concave   1
    # return a**2