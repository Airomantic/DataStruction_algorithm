"""
最小生成树： 1 既是树则不能出现环  2 n个结点n-1条边的权重和最小
https://www.bilibili.com/video/BV1Eb41177d1?from=search&seid=12360573940338853733&spm_id_from=333.337.0.0
kruskal: 直接选择权重最小的边
prim :间接选择与顶点相连权重最小的边
1 选择一个初始顶点与其直接相连的顶点最为一个集合A，另一个不与这个集合A中所有顶点相连的集合B，
2 然后选取集合A和集合B之间最小权重边，
3 每选好一个新的边连接的顶点将加入集合A形成新的集合A，再重复进行2

结点：0 1 2 3 4
一般 Prim 邻接表时间复杂度是O(n^2) 继续优化是O(n*log n)
Prim 邻接矩阵时间复杂度是O()
"""
INF = 9999999


class Gragh:
    def __init__(self, V, G):
        self.V = V
        self.G = G

    def prim(self):
        selected = [0] * self.V
        no_edge = 0
        selected[0] = True  # 第一个赋成True
        print("Edge : Weight")
        # 需要选择V-1个
        while no_edge < self.V - 1:
            minimum = INF
            x, y = 0, 0
            # 遍历V个节点
            for i in range(V):  # 这个直接来源于参数V =5 不能变动，self.V可以变
                # 该节点选择了的
                if selected[i]:
                    for j in range(self.V):
                        # 选择的邻接节点没有选择的，且有边
                        if (not selected[j]) and self.G[i][j]:
                            if minimum > self.G[i][j]:
                                minimum = self.G[i][j]  # 更新
                                x, y = i, j
            print(str(x) + "-" + str(y) + ":" + str(self.G[x][y]))
            selected[y] = True #已选过的
            no_edge += 1 #直到连完所有结点

if __name__ == '__main__':
    V = 5  # 结点数量
    """邻接矩阵"""
    # 无向有权图 权重二维数组
    G = [[0, 9, 75, 0, 0],
         [9, 0, 95, 19, 42],
         [75, 95, 0, 51, 66],
         [0, 19, 51, 0, 31],
         [0, 42, 66, 31, 0]]
    graph = Gragh(V, G)
    graph.prim()
