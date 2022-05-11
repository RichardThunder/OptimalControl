import networkx as nx
#使用networkx 将文件中的边转换成图
def Get_arenas_email_Network(path):

    G=nx.Graph()

    Edge_Lists=[]
    node_set = set()
    with open(path,'r') as f:
        for line in f:
            cols=line.strip().split(' ')
            X1=int(cols[0])
            X2=int(cols[1])
            node_set.add(X1)
            node_set.add(X2)
            edge=(X1,X2)
            Edge_Lists.append(edge)

    G.add_nodes_from(range(1,len(node_set)+1)) #节点序号从1开始
    G.add_edges_from(Edge_Lists)

    A=nx.adjacency_matrix(G).todense()
    #print(A)

    #List of degree
    degree_List=[]
    for node in G:
        degree=G.degree(node)
        degree_List.append(degree)
    #print(degree_List)

    return A,degree_List,Edge_Lists,G
#查看获取的图是否正确
#print(Get_arenas_email_Network()[0])
