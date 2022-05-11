import networkx as nx
import pandas as pd
from net.LoadGraph import Get_arenas_email_Network
from pylab import *
import matplotlib.pyplot as plt

def Graph():
    G = Get_arenas_email_Network()[0]
    G=nx.Graph(G)
    Graph=np.asarray(G)
    Graph_data=pd.DataFrame(Graph)
    Graph_data.to_csv("./OPtr/Graph.csv")


# # #pos = nx.circular_layout(G)
# # pos=nx.shell_layout(G)
# #
# # nx.draw(G, pos, node_color=range(100),edge_color='b',node_size=40, cmap=plt.cm.Blues)
# # plt.show()
#
#


def drawClub(G):
    options = {"node_color": "green", "node_size": 50, "linewidths": 0, "width": 0.3, "alpha": 1,"edge_color": "orange"}
    nx.draw_circular(G, with_labels=False,**options)
    plt.savefig("./net/club.png")


def football(G):
    # football
    options = {"node_color": "blue", "node_size": 50, "linewidths": 0, "width": 0.3,"alpha":0.7}

    pos = nx.spring_layout(G,1969)  # Seed for reproducible layout
    nx.draw(G, pos, **options)
    plt.savefig("football.png")
    #plt.show()

def ThreeD(G):
    # 3d spring layout
    pos = nx.spring_layout(G, dim=3, seed=779)
    # Extract node and edge positions from the layout
    node_xyz = np.array([pos[v] for v in sorted(G)])
    edge_xyz = np.array([(pos[u], pos[v]) for u, v in G.edges()])

    # Create the 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the nodes - alpha is scaled by "depth" automatically
    ax.scatter(*node_xyz.T, s=50, ec="b")

    # Plot the edges
    for vizedge in edge_xyz:
        ax.plot(*vizedge.T, color="tab:gray")


    def _format_axes(ax):
        """Visualization options for the 3D axes."""
        # Turn gridlines off
        ax.grid(False)
        # Suppress tick labels
        for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
            dim.set_ticks([])
        # Set axes labels
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")


    _format_axes(ax)
    fig.tight_layout()
    fig.savefig("3D.png")
    plt.show()




def drawtest():
    figure(figsize=(16,6),dpi=80)
    subplot(1,1,1)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # 添加图例
    plt.plot(X,C,color="blue",linewidth=2.5,linestyle="--",label="cosine")
    plt.plot(X,S, color="green", linewidth=2.5, linestyle="-",label="sine")
    legend(loc='upper right')
    xmin,xmax=X.min(),X.max()
    ymin,ymax=C.min(),C.max()
    dx = (xmax - xmin) * 0.2
    dy = (ymax - ymin) * 0.2
    # 设置上下限
    xlim(xmin - dx, xmax + dx)
    ylim(ymin - dy, ymax + dy)


    #设置横轴标记
    # xticks(np.linspace(-4,4,9,endpoint=True))
    # yticks(np.linspace(-1,1,5,endpoint=True))
    # xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
    # yticks([-1,0,1])
    ##using latex
    xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])
    plt.show()

if __name__ == "__main__":
    #path="/Users/richard/Desktop/OptCtrl/net/realWorld.txt"
    path="/Users/richard/Desktop/OptCtrl/net/short_social.txt"
    #path="/Users/richard/Desktop/OptCtrl/net/scaleFree.txt"
    graph=Get_arenas_email_Network(path)[3]
    drawClub(graph)




