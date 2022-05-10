import numba

from Psi import Psi
from Phi import Phi

@numba.jit
def FM(t, i, Graph, alpha, beta, a, b, Uncompromised, gamma, delta, L, M):
    N = len(Graph)
    sum1 = 0
    for j in range(0, N):
        sum1 = sum1 + beta * Graph[[i], [j]] * Uncompromised[[t], [j]] * (L[[t], [j]] - M[[t], [j]])
    return -a + b - Phi(
        delta[[t], [i]]) + Psi(gamma[[t], [i]]) + gamma[[t], [i]] * L[[t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1