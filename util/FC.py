import numba


@numba.jit
# FC
# t - - 时刻t
# i - - 处理第i个节点
# alpha, beta - - 感染率和传染率
# A - - 网络结构
def FC(t, i, alpha, beta, Graph, Compromised, Uncompromised, delta):
    N = len(Graph)
    sum1 = 0
    for j in range(0, N):
        sum1 = sum1 + Graph[[i], [j]] * Compromised[[t], [j]]
    return (alpha + beta * sum1) * Uncompromised[[t], [i]] - delta[[t], [i]] * Compromised[[t], [i]]

