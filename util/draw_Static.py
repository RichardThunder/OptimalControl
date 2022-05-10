import pandas as pd


def draw_StaCtrl(DG, Con_Phi, Con_Psi):
    StaticPath = "./Static/"

    OJ = DG[0]
    EP = DG[1]


    print("Complete")
    print("writing CSV...")

    print("Save OJ")
    OJ_data = pd.DataFrame(OJ)
    OJ_data.to_csv(StaticPath+'Sta_OJ_'+'Phi_'+str(Con_Phi)+'_Psi_'+str(Con_Phi)+'.csv')

    print("Save EP")
    EP_data = pd.DataFrame(EP)
    EP_data.to_csv(StaticPath+'Sta_EP_'+'Phi_'+str(Con_Phi)+'_Psi_'+str(Con_Phi)+'.csv')


