from numba import jit
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



def OptimalControl_Euler(T, h, maxTimes, Graph, u_init, c_init, alpha, beta, delta_init, gamma_init,Con_Phi,Con_Psi,delta_min,delta_max,gamma_min,gamma_max):
    # 参数初始化
    # GlobalVar.set_value('Uninfected',u_init*mat(ones((n,N))))
    # GlobalVar.set_value('Infected',c_init*mat(ones((n,N))))
    # GlobalVar.set_value('L',mat(zeros((n,N))))
    # GlobalVar.set_value('M',mat(zeros((n,N))))
    # GlobalVar.set_value('delta',delta_init*mat(ones((n,N))))
    # GlobalVar.set_value('gamma',gamma_init*mat(ones((n,N))))




    print('执行最优控制')
    t0 = np.arange(0, T + h, h)
    n = len(t0)
    N = len(Graph)

    Uninfected=u_init*np.ones((n,N))
    Infected=c_init*np.ones((n,N))
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

    #gamma_last =np.repeat(gamma,1)
    #delta_last =np.repeat(delta,1)
    gamma_last=np.tile(gamma,1)
    delta_last=np.tile(gamma,1)
    LOOP0_n = np.arange(0, n)
    LOOP0_N = np.arange(0, N)
    LOOP0_Max = np.arange(0, maxTimes)
    LOOP1_n = np.arange(1, n)
    LOOP0_n_1 = np.arange(0, n - 1)
    LOOP_back = np.arange(n - 1, 0, -1)
    # 最优控制迭代
    for tt in LOOP0_Max:
        if flag == 0:
            break

        print('最优控制第', tt + 1, '次迭代')
        #print("更新Infected && Uninfected")
        for t in tqdm(LOOP0_n_1,  desc="更新Infected && Uninfected"):
            # 更新Infected

            for i in LOOP0_N:
                y = Infected[[t], [i]]

                # FC#############
                # result = y + h * FC(t, i, alpha, beta, Graph, Infected, Uninfected, delta)
                sum1=0
                for j in LOOP0_N:
                    sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]

                FC=(alpha + beta * sum1) * Uninfected[[t], [i]] - delta[[t], [i]] * Infected[[t], [i]]

                result =y + h * FC
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
                sum1=0
                for j in LOOP0_N  :
                    sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
                    result =y + h * gamma[[t], [i]] * (
                            1 - Uninfected[[t], [i]] - Infected[[t], [i]]) - (alpha + beta * sum1) * Uninfected[
                        [t], [i]]
                #################################
                if result > 1:
                    Uninfected[[t + 1], [i]] = 1
                elif result < 0:
                    Uninfected[[t + 1], [i]] = 0
                else:
                    Uninfected[[t + 1], [i]] = result

        #print("更新 Lambda && Mu")
        # 更新lambda，mu
        for t in tqdm(LOOP_back, desc="更新"+chr(955)+" && "+chr(956)):
            # lambda
            for i in LOOP0_N:
                y = L[[t], [i]]
                ##FL###########################################
                # L[[t - 1], [i]] = y - h * FL(t, i, Graph, alpha, beta, a[i], b[i], Infected, gamma, L, M)
                sum1 = 0
                for j in LOOP0_N:
                    sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
                if Con_Psi == 0:  # convex
                    FL = b[i] + np.sqrt(gamma[[t], [i]]) + gamma[[t], [i]] * L[[t], [i]] + (alpha + beta * sum1) * (
                                L[[t], [i]] - M[[t], [i]])
                elif Con_Psi == 1:  # concave
                    FL = b[i] + np.power(gamma[[t], [i]], 2) + gamma[[t], [i]] * L[[t], [i]] + (alpha + beta * sum1) * (
                                L[[t], [i]] - M[[t], [i]])

                L[[t - 1], [i]] = y - h * FL
            # mu
            for i in LOOP0_N:
                y = M[[t], [i]]
                # FM
                # M[[t - 1], [i]] = y - h * FM(t, i, Graph, alpha, beta, a[i], b[i], Uninfected, gamma, delta, L, M)
                sum1 = 0
                for j in LOOP0_N:
                    sum1 = sum1 + beta * Graph[[i], [j]] * Uninfected[[t], [j]] * (L[[t], [j]] - M[[t], [j]])
                    # Convex = 0 OR Concave = 1  Phi && Psi
                    if Con_Psi == 0 and Con_Phi == 0:
                        FM = -a[i] + b[i] - np.sqrt(delta[[t], [i]]) + np.sqrt(gamma[[t], [i]]) + gamma[[t], [i]] * L[
                            [t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1
                    elif Con_Psi == 1 and Con_Phi == 0:
                        FM = -a[i] + b[i] - np.sqrt(delta[[t], [i]]) + np.power(gamma[[t], [i]], 2) + gamma[[t], [i]] * L[
                            [t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1
                    elif Con_Psi == 0 and Con_Phi == 1:
                        FM = -a[i] + b[i] - np.power(delta[[t], [i]] , 2) + np.sqrt(gamma[[t], [i]]) + gamma[[t], [i]] * L[
                            [t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1
                    elif Con_Psi == 1 and Con_Phi == 1:
                        FM = -a[i] + b[i] - np.power(delta[[t], [i]],  2) + np.power(gamma[[t], [i]] , 2) + gamma[[t], [i]] * L[
                            [t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1

                M[[t - 1], [i]] = y - h * FM

        # 更新delta和gamma
        # 凹函数和凸函数之选其一，注意统一凹凸性
        # 注意凹凸性与Phi和Psi函数相同
        #print("更新delta && Gamma")
        # delta
        # ######################################################################################################
        if Con_Phi == 0:
            temp_theta = (np.sqrt(delta_max) - np.sqrt(delta_min)) / (delta_max - delta_min)
        elif Con_Phi == 1:
            temp_theta = (np.power(delta_max , 2) - np.power(delta_min , 2)) / (delta_max - delta_min)
        # 凸函数
        if Con_Phi == 1:
            for t in tqdm(LOOP1_n,desc="更新"+chr(948)):
                for i in LOOP0_N:
                    if Infected[[t], [i]] == 0 or M[[t], [i]] <= temp_theta:
                        delta[[t], [i]] = delta_min
                    elif Infected[[t], [i]] > 0 and M[[t], [i]] > temp_theta:
                        delta[[t], [i]] = delta_max
        elif Con_Phi == 0:
            # 凹函数
            for t in tqdm(LOOP1_n , desc="更新"+chr(948)):
                for i in LOOP0_N:
                    if Infected[[t], [i]] == 0 or M[[t], [i]] < 2 * delta_min:
                        delta[[t], [i]] = delta_min
                    elif Infected[[t], [i]] > 0 and M[[t], [i]] > 2 * delta_max:
                        delta[[t], [i]] = delta_max
                    else:
                        delta[[t], [i]] = 0.5 * M[[t], [i]]

        # gamma
        if Con_Psi == 0:
            temp_eta = (np.sqrt(gamma_max) - np.sqrt(gamma_min)) / (gamma_max - gamma_min)
        elif Con_Psi == 1:
            temp_eta = (np.power(gamma_max , 2) - np.power(gamma_min , 2)) / (gamma_max - gamma_min)
        # 凸函数
        if Con_Psi == 0:
            for t in tqdm(LOOP1_n,desc="更新"+chr(947)):
                for i in LOOP0_N:
                    if (Infected[[t], [i]] + Uninfected[[t], [i]] == 1) or (L[[t], [i]] >= -temp_eta):
                        gamma[[t], [i]] = gamma_min
                    elif (Infected[[t], [i]] + Uninfected[[t], [i]] <1) and (L[[t], [i]] < -temp_eta):
                        gamma[[t], [i]] = gamma_max
        elif Con_Psi == 1:
            # 凹函数
            for t in tqdm(LOOP1_n, desc="更新"+chr(947)):
                for i in LOOP0_N:
                    if (Infected[[t], [i]] + Uninfected[[t],[i]] == 1) or (L[[t], [i]] > -2 * gamma_min):
                        gamma[[t], [i]] = gamma_min
                    elif (Infected[[t], [i]] + Uninfected[[t], [i]] <1)and (L[[t], [i]] < -2 * gamma_max):
                        gamma[[t], [i]] = gamma_max
                    else:
                        gamma[[t], [i]] = 0.5 * (-L[[t], [i]])

        EP = np.mat(zeros((n, 1)))
        Lxt = np.mat(zeros((n, 1)))

        #print("计算损失")
        # 计算损失 每时刻损失
        for t in tqdm(LOOP0_n, desc="更新损失loss"):
            sum1 = 0
            for i in LOOP0_N :
                if Con_Phi == 0:
                    sum1 = sum1 + (a[i] + np.sqrt(delta[[t], [i]])) * Infected[[t], [i]]
                elif Con_Phi == 1:
                    sum1 = sum1 + (a[i] + np.power(delta[[t], [i]] ,2)) * Infected[[t], [i]]
            sum2 = 0
            for i in LOOP0_N:
                if Con_Psi == 0:
                    sum2 = sum2 + (b[i] + np.sqrt(gamma[[t], [i]])) * (
                                1 - Uninfected[[t], [i]] - Infected[[t], [i]])
                elif Con_Psi == 1:
                    sum2 = sum2 + (b[i] + np.power(gamma[[t], [i]] , 2)) * (
                                1 - Uninfected[[t], [i]] - Infected[[t], [i]])
            Lxt[t] = sum1 + sum2

        EP[0] = Lxt[0]
        for j in LOOP0_n:
            EP[j] = EP[j-1] + Lxt[j]
        OJS[[tt],[0]] = EP[n-1]
        print("\n退出循环判断")
        # 推出循环判断
        delta_inc = np.abs(delta - delta_last)
        gamma_inc = np.abs(gamma - gamma_last)
        if (np.sum(delta_inc[:]) + np.sum(gamma_inc[:])) / 10000 < 1e-4:
            flag = 0
            print("\n退出循环")
        #delta_last = np.repeat(delta,1)
        # gamma_last = np.repeat(gamma,1)
        gamma_last = np.tile(gamma, 1)
        delta_last = np.tile(gamma, 1)
    EP = np.zeros((n, 1))
    Lxt = np.zeros((n, 1))

    for t in LOOP0_n:
        sum1 = 0
        for i in LOOP0_N:
            if Con_Phi == 0:
                sum1 = sum1 + (a[i] + np.sqrt(delta[[t], [i]])) * Infected[[t], [i]]
            elif Con_Phi == 1:
                sum1 = sum1 + (a[i] + np.power(delta[[t], [i]], 2)) * Infected[[t], [i]]
        sum2 = 0
        for i in LOOP0_N:
            if Con_Psi == 0:
                sum2 = sum2 + (b[i] + np.sqrt(gamma[[t], [i]])) * (1 - Uninfected[[t], [i]] - Infected[[t], [i]])
            elif Con_Psi == 1:
                sum2 = sum2 + (b[i] + np.power(gamma[[t], [i]], 2)) * (1 - Uninfected[[t], [i]] - Infected[[t], [i]])
        Lxt[t] = sum1 + sum2

    EP[0] = Lxt[0]

    for j in LOOP1_n:
        EP[j] = EP[j - 1] + Lxt[j]
    OJ = EP[n-1]

    return delta, gamma,OJ,EP,OJS,Lxt



#  t -- 时刻t
#   i -- 处理第i个节点
#   alpha, beta -- 感染率和传染率
#   gamma -- 回复比率
#   Graph -- 网络结构
@jit
def FU(t, i, alpha, beta, Graph, Infected, Uninfected, gamma):
    N = len(Graph)
    LOOP0_N = np.arange(0, N)
    sum1 = 0
    for j in LOOP0_N:
        sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
    return gamma[[t], [i]] * (
            1 - Uninfected[[t], [i]] - Infected[[t], [i]] - (alpha + beta * sum1) * Uninfected[[t], [i]])


# FC
# t - - 时刻t
# i - - 处理第i个节点
# alpha, beta - - 感染率和传染率
# A - - 网络结构
@jit
def FC(t, i, alpha, beta, Graph, Infected, Uninfected, delta):
    N = len(Graph)
    LOOP0_N = np.arange(0, N)
    sum1 = 0
    for j in LOOP0_N:
        sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
    return (alpha + beta * sum1) * Uninfected[[t], [i]] - delta[[t], [i]] * Infected[[t], [i]]


#   t -- 时刻t
#   i -- 处理第i个节点
#   alpha, beta -- 感染率和传染率
#   a, b -- 入侵损失和隔离损失
#   A -- 网络结构
@jit
def FL(t, i, Graph, alpha, beta, a, b, Infected, gamma, L, M):
    N = len(Graph)
    LOOP0_N = np.arange(0, N)
    sum1 = 0
    for j in LOOP0_N:
        sum1 = sum1 + Graph[[i], [j]] * Infected[[t], [j]]
    return b + Psi(
        gamma[[t], [i]]) + gamma[[t], [i]] * L[[t], [i]] + (alpha + beta * sum1) * (L[[t], [i]] - M[[t], [i]])

@jit
def FM(t, i, Graph, alpha, beta, a, b, Uninfected, gamma, delta, L, M):
    N = len(Graph)
    LOOP0_N = np.arange(0, N)
    sum1 = 0
    for j in LOOP0_N:
        sum1 = sum1 + beta * Graph[[i], [j]] * Uninfected[[t], [j]] * (L[[t], [j]] - M[[t], [j]])
    return -a + b - Phi(
        delta[[t], [i]]) + Psi(gamma[[t], [i]]) + gamma[[t], [i]] * L[[t], [i]] + delta[[t], [i]] * M[[t], [i]] + sum1

@jit
def Psi(a):
    # convex
    return np.sqrt(a)

    # concave
    # return np.power(a,2)

@jit
def Phi(a):
    # convex
    return np.sqrt(a)

# concave
# return np.power(a,2)
