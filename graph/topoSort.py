"""
拓扑排序
有向图没有变成，即无权重
"""
def topoSort(graph):

    in_degress=dict((u,0) for u in graph)#初始化所有顶点入度为0
    num = len(in_degress)
    for u in graph:
        for v in graph[u]:
            in_degress[v] +=1
    #筛选入度为0的顶点
    Q = [u for u in in_degress if in_degress[u] == 0]
    seq = []
    #列出所有边
    while Q:
        u = Q.pop()
        seq.append(u)
        for v in graph[u]:
            in_degress[v] -= 1
            if in_degress[v] == 0: #再次筛选入度为0的顶点
                Q.append(v)

    #判断输出的顶点数是否与图中的顶点数相等
    if len(seq) == num:
        return seq
    else:
        return None

G ={
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}

print(topoSort(G))
