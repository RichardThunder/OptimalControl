
#  t -- 时刻t
#   i -- 处理第i个节点
#   alpha, beta -- 感染率和传染率
#   gamma -- 回复比率
#   Graph -- 网络结构
import numba


@numba.jit
def FU(t, i, alpha, beta, Graph, Compromised, Uncompromised, gamma):
    N = len(Graph)

    sum1 = 0
    for j in range(0, N):
        sum1 = sum1 + Graph[[i], [j]] * Compromised[[t], [j]]
    return gamma[[t], [i]] * (
            1 - Uncompromised[[t], [i]] - Compromised[[t], [i]] - (alpha + beta * sum1) * Uncompromised[[t], [i]])
