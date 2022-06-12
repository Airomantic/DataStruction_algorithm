"""
https://www.bilibili.com/video/BV1ts41157Sy/?spm_id_from=autoNext
优先队列：重要性质是"插队"，其内部原理是"普通队列+堆排序" 实现的，只有弹出出来时才有顺序，直接打印优先队列是无序的
"""
import heapq
import math

"""
设置二维字典{{}}
无向有权图
"""
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}
# print(graph["A"])
# print(graph["A"].keys())
# print(graph["A"]["B"]) #A和B的距离
"""
一开始distance只记录了一个点，如果一个结点没出现distance[w] = dist + graph[vertex][w]就会下标越界indexError
要把剩下的点标为正无穷 整型正无穷
"""
def init_distance(graph,start):
    distance = {start:0}
    for vertex in graph:
        if vertex != start:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph,start):
    pqueue = []
    heapq.heappush(pqueue,(0,start) ) #(0,start) 第一个参数是0表示初始时，当前点与起始点距离为0
    seen = set()
    #seen.add(start) #被放进去多次的结点，如果没有被拿出来，仍算作没有被看到，只有弹出来后才算看到，所以不能在这里就放入
    parent = {start: None} #起始点的前一个点是空
    distance = init_distance(graph,start)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue) #拿到的是一对结点，其之间的距离和当前点
        dist,vertex = pair[0],pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] <distance[w]:
                    heapq.heappush(pqueue,(dist + graph[vertex][w],w))
                    parent[w] = vertex #w的前一个点就是vertex
                    distance[w] = dist + graph[vertex][w]
    return parent,distance

parent,distance =dijkstra(graph,"A")
print(parent)
print(distance)
v = 'F'
while v!= None:
    print(v)
    v = parent[v]