"""
实现思路
输入：图
输出：最小树
最小树满足条件：
   包含了所有的节点
   在图构成的所有树中，是总分值最小的树
实现步骤:
1 对所有的边根据权重进行从小到大排序
2 每次选择最小的边加入到树中，如果新增加的边导致树中有环，则丢弃该条边
3 重复上面2增加边的操作，直到树包含了所有的节点
https://www.bilibili.com/video/BV1Eb41177d1?from=search&seid=12360573940338853733&spm_id_from=333.337.0.0
基于并查集
https://blog.csdn.net/weixin_40673608/article/details/85308236
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # 定义个数组graph

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # 找到节点所在的树的根节点
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])  # 递归

    # 合并新的节点到一棵树中来 即类似于prim的已选集合
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def Kruskal(self):
        result = []
        i, e = 0, 0
        # 排序，边按照权重从小到大排序
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        # 初始，每个节点构成一棵树，根节点就是自己
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # 做V-1条节点选择
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # 选择的边的两个节点不在同一棵树,则合并
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)  # 不能出现环
        # 打印每一次选择的边
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


if __name__ == '__main__':
    g = Graph(6)  # 类的括号里传参，直接传给构造方法,即self.V = 6 所以共6个结点0 1 2 3 4 5
    """邻接表"""
    for x, y, w in [(0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 0, 4), (2, 0, 4), (2, 1, 2), (2, 3, 3), (2, 5, 2), (2, 4, 4),
                    (3, 2, 3), (3, 4, 3), (4, 2, 4), (4, 3, 3), (5, 2, 2), (5, 4, 3)]:
        g.add_edge(x, y, w)
    g.Kruskal()
