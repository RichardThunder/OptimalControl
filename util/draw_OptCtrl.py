import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import *


def draw_OptCtrl(DG,Con_Phi,Con_Psi):
    OptrPath="./OPtr/"
    delta = DG[0]
    gamma = DG[1]
    OJ = DG[2]
    EP = DG[3]
    OJS = DG[4]
    LXT = DG[5]

    print("Complete")
    print("writing CSV...")

    delta_data = pd.DataFrame(delta)
    delta_data.to_csv(OptrPath + 'delta_Phi_' + str(Con_Phi) + '_Psi_' + str(Con_Psi) + '.csv')
    gamma_data = pd.DataFrame(gamma)
    gamma_data.to_csv(OptrPath + 'gamma_Phi_' + str(Con_Phi) + '_Psi_' + str(Con_Psi) + '.csv')

    print("Save OJ")
    OJ_data = pd.DataFrame(OJ)
    OJ_data.to_csv(OptrPath +'Opt_OJ.csv')

    print("Save EP")
    EP_data = pd.DataFrame(EP)
    EP_data.to_csv(OptrPath +'Opt_EP.csv')

    print("Save OJS")
    OJS_data = pd.DataFrame(OJS)
    OJS_data.to_csv(OptrPath +'Op_OJS.csv')

    print("Save LXT")
    LXT_data = pd.DataFrame(LXT)
    LXT_data.to_csv(OptrPath +'Opt_LXT.csv')

    N=delta.shape

    for i in range(N[1]):
        figure(figsize=(4, 3), dpi=400)#1200*800
        ax = plt.gca()  # gca:get current axis得到当前轴
        # 设置图片的右边框和上边框为不显示
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.plot(np.arange(N[0]),delta[:,[i]], color="blue", linewidth=3, linestyle="-", label=r"$\delta$")
        plt.plot(np.arange(N[0]),gamma[:,[i]], color="red", linewidth=3, linestyle="-", label=r"$\gamma$")
        legend(loc=(0.9,0.9),frameon=False)
        plt.savefig('./OPtr/'+str(i)+'.png')
