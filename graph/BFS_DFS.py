"""
https://www.bilibili.com/video/BV1Ks411579J?spm_id_from=333.999.0.0
BFS：queue
DFS：stack 也是一种回溯
哈希表查找快于数组
以下为无权重无向图
"""
# z=字典
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}
# 查看所有结点-数组
print(graph.keys())
# 链接点
print(graph["E"])
"""
BFS是分层的
"""


def BFS(graph, start):  # start一开始是起始结点，之后该变量用于记录结点是否被看到过  vertex顶点
    queue = []  # python的数组可以动态删除或插入 pop(0)弹出append进去的第一个元素
    queue.append(start)
    seen = set()  # 来看一下已经访问过哪些结点，{}哈希表集合set
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop(0)  # 弹出最先进去的元素
        nodes = graph[vertex] #找到vertex的邻接点
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


"""
BFS做映射一个字典parent{}，它每次记录 当前点的前一个点是那个点
"""


def BFS_minPath(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start: None} #起始点的前一个点是空
    while len(queue) > 0:
        vertex = queue.pop(0)  # 弹出最先进去的元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex #w的前一个点就是vertex
        print(vertex)
    return parent

def DFS(graph, start):  # start一开始是起始结点，之后该变量用于记录结点是否被看到过  vertex顶点
    stack = []  # python的数组可以动态删除或插入 pop(0)弹出append进去的最后一个元素
    stack.append(start)
    seen = set()  # 来看一下已经访问过哪些结点，{}哈希表集合set
    seen.add(start)
    while len(stack) > 0:
        vertex = stack.pop()  # 把pop(0)中的0去掉 弹出栈顶元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

# BFS(graph,"A")
# DFS(graph, "A")
parent = BFS_minPath(graph,"E")
#hashMap是无序的，每次打印的顺序都不相同
for key in parent:
    print((key,parent[key]))
#顶点"E" -> "B"
v = 'B'
while v!= None:
    print(v)
    v = parent[v]