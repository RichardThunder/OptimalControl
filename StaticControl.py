from numpy import *
import numba as nb
import numpy as np


# h: 步长, dt
# n: 时间长度
# N: 节点个数
# u_init     初始未被感染的概率
# c_init     初始被感染的概率
# alpha      节点感染率
# beta2      节点传染率
# delta_init 初始隔离率
# gamma_init 初始回复率
# Graph          网络矩阵
from tqdm import tqdm
@nb.jit
def StaticControl(T, h, maxTimes, Graph, u_init, c_init, alpha, beta, delta_init, gamma_init,Con_Phi,Con_Psi):
    # 参数初始化
    # GlobalVar.set_value('Uninfected',u_init*mat(ones((n,N))))
    # GlobalVar.set_value('Infected',c_init*mat(ones((n,N))))
    # GlobalVar.set_value('L',mat(zeros((n,N))))
    # GlobalVar.set_value('M',mat(zeros((n,N))))
    # GlobalVar.set_value('delta',delta_init*mat(ones((n,N))))
    # GlobalVar.set_value('gamma',gamma_init*mat(ones((n,N))))
    print("执行静态控制")
    t0 = np.arange(0, T + h, h)
    n = len(t0)
    N = len(Graph)

    Uninfected = u_init * np.ones((n, N))
    Infected = c_init * np.ones((n, N))
    L = np.zeros((n, N))  # lambda
    M = np.zeros((n, N))  # mu
    delta = delta_init * np.ones((n, N))
    gamma = gamma_init * np.ones((n, N))
    # 感染损失
    a = np.random.rand(N, 1) * 3
    # 隔离损失
    b = np.random.rand(N, 1)

    OJS = np.zeros((maxTimes, 1))

    flag = 1
    # gamma_last =np.repeat(gamma,1)
    # delta_last =np.repeat(delta,1)
    gamma_last = np.tile(gamma, 1)
    delta_last = np.tile(gamma, 1)
    LOOP0_n = np.arange(0, n)
    LOOP0_N = np.arange(0, N)
    LOOP0_Max = np.arange(0, maxTimes)
    LOOP1_n = np.arange(1, n)
    LOOP0_n_1 = np.arange(0, n - 1)
    LOOP_back = np.arange(n - 1, 0, -1)

    for t in tqdm(LOOP0_n_1,  desc="更新Infected && Uninfected"):
        # 更新Infected

        for i in LOOP0_N:
            y = Infected[[t], [i]]

            # FC#############
            # result = y + h * FC(t, i, alpha, beta, Graph, Infected, Uninfected, delta)
            sum1 = 0
            for j in LOOP0_N:
                sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]

            FC = (alpha + beta * sum1) * Uninfected[[t], [i]] - delta[[t], [i]] * Infected[[t], [i]]

            result = y + h * FC
            #################################
            if result > 1:
                Infected[[t + 1], [i]] = 1
            elif result < 0:
                Infected[[t + 1], [i]] = 0
            else:
                Infected[[t + 1], [i]] = result

        # 更新Uninfected
        for i in LOOP0_N:
            y = Uninfected[[t], [i]]
            ###FU###########
            # result = y + h * FU(t, i, alpha, beta, Graph, Infected, Uninfected, gamma)
            sum1 = 0
            for j in LOOP0_N:
                sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
                result = y + h * gamma[[t], [i]] * (
                        1 - Uninfected[[t], [i]] - Infected[[t], [i]]) - (alpha + beta * sum1) * Uninfected[
                             [t], [i]]
            #################################
            if result > 1:
                Uninfected[[t + 1], [i]] = 1
            elif result < 0:
                Uninfected[[t + 1], [i]] = 0
            else:
                Uninfected[[t + 1], [i]] = result

    EP = np.zeros((n, 1))
    Lxt = np.zeros((n, 1))
    # print("计算损失")
    # 计算损失 每时刻损失
    for t in tqdm(LOOP0_n, desc="更新损失loss"):
        sum1 = 0
        for i in LOOP0_N:
            if Con_Phi == 0:
                sum1 = sum1 + (a[i] + np.sqrt(delta[[t], [i]])) * Infected[[t], [i]]
            elif Con_Phi == 1:
                sum1 = sum1 + (a[i] + np.power(delta[[t], [i]], 2)) * Infected[[t], [i]]
        sum2 = 0
        for i in LOOP0_N:
            if Con_Psi == 0:
                sum2 = sum2 + (b[i] + np.sqrt(gamma[[t], [i]])) * (
                        1 - Uninfected[[t], [i]] - Infected[[t], [i]])
            elif Con_Psi == 1:
                sum2 = sum2 + (b[i] + np.power(gamma[[t], [i]], 2)) * (
                        1 - Uninfected[[t], [i]] - Infected[[t], [i]])
        Lxt[t] = sum1 + sum2

    EP[0] = Lxt[0]
    for j in LOOP1_n:
        EP[j] = EP[j - 1] + Lxt[j]
    OJ = EP[n-1]

    return OJ,EP
