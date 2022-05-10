import pandas as pd
from numpy import *
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from StaticControl import StaticControl
from net.LoadGraph import *
from OptimalControl_Euler import OptimalControl_Euler
import warnings

from util.draw import football, drawCircle
from util.draw_OptCtrl import draw_OptCtrl
from util.draw_Static import draw_StaCtrl

def CompareMain():
    warnings.filterwarnings('ignore')

    #path= './net/short_social.txt'
    path='./net/scaleFree.txt'
    #path='./net/realWorld.txt'
    Graph = Get_arenas_email_Network(path)[0]

    #football(Graph)
    #drawCircle(Graph)
    # argument
    T = 10
    #h = 0.01
    h=1
    xtk = np.arange(0, T + h, h)
    n=len(xtk)
    maxTimes=10

    # 模型参数
    u_init = 0.8    #初始未被感染的概率
    c_init = 0.1    # 初始被感染的概率
    alpha = 0.1    #节点感染率
    beta = 0.2     # 节点传染率
    delta_init = 0.5   # 初始隔离率
    gamma_init = 0.4   # 初始回复率

    # Convex = 0 OR Concave = 1  Phi && Psi
    Con_Phi = 1
    Con_Psi = 1

    # 设置delta和gamma 的上下限
    delta_min = 0.2
    delta_max = 1.2
    gamma_min = 0.1
    gamma_max = 1

    #GlobalVar._init()
    print("加载网络")
    Graph=np.asarray(Graph)
    # delta == chr(948) gamma=chr(947)
    print(chr(948)+"下限为："+str(delta_min)+"    "+chr(948)+"上限为："+str(delta_max))
    print(chr(947)+"下限为："+str(gamma_min)+"    "+chr(947)+"上限为："+str(gamma_max))
    print("加载控制模型")


###OPT 返回值是tuple 依次为 （delta, gamma,OJ,EP,OJS,Lxt）
    OPT=OptimalControl_Euler(T,h,maxTimes,Graph,u_init,c_init,alpha,beta,delta_init,gamma_init,Con_Phi,Con_Psi,delta_min,delta_max,gamma_min,gamma_max)
    draw_OptCtrl(OPT,Con_Phi,Con_Psi)

    ###########STA 返回值是元组 依次为（OJ,EP）
    STA1=StaticControl(T, h, maxTimes, Graph, u_init, c_init, alpha, beta, 1.2,1,Con_Phi,Con_Psi)
    draw_StaCtrl(STA1,Con_Phi,Con_Psi)
    STA2=StaticControl(T, h, maxTimes, Graph, u_init, c_init, alpha, beta, 0.7,0.55,Con_Phi,Con_Psi)
    draw_StaCtrl(STA2,Con_Phi,Con_Psi)
    STA3=StaticControl(T, h, maxTimes, Graph, u_init, c_init, alpha, beta, 0.2,0.1,Con_Phi,Con_Psi)
    draw_StaCtrl(STA3,Con_Phi,Con_Psi)

    #静态控制对比
    figure(figsize=(4,3),dpi=100)
    subplot(1,1,1)
    #EP
    X=np.arange(0,T/h+1)
    y_opt=OPT[3]

    #Ep
    y_sta1=STA1[1]
    y_sta2=STA2[1]
    y_sta3=STA3[1]

    plt.plot(X,y_opt,color="blue",linewidth=2,linestyle="-",label="OPT")
    plt.plot(X,y_sta1,color="green",linewidth=2,linestyle="-.",label="Static1")
    plt.plot(X,y_sta2,color="red",linewidth=2,linestyle=":",label="Static2")
    plt.plot(X,y_sta3,color="black",linewidth=2,linestyle="--",label="Static3")
    legend(loc="upper left",frameon=False)
    plt.savefig("Compare_Opt_Sta.png")


    print("Program Exit")


if __name__=="__main__":
    CompareMain()