import numba

from Psi import Psi


#   t -- 时刻t
#   i -- 处理第i个节点
#   alpha, beta -- 感染率和传染率
#   a, b -- 入侵损失和隔离损失
#   A -- 网络结构
@numba.jit
def FL(t, i, Graph, alpha, beta, a, b, Compromised, gamma, L, M):
    N = len(Graph)

    sum1 = 0
    for j in range(0, N):
        sum1 = sum1 + Graph[[i], [j]] * Compromised[[t], [j]]
    return b + Psi(
        gamma[[t], [i]] + gamma[[t], [i]] * L[[t], [i]] + (alpha + beta * sum1) * (L[[t], [i]] - M[[t], [i]]))
