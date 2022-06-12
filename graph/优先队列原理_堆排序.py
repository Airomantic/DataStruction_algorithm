
"""
优先队列：重要性质是"插队"，其内部原理是"普通队列+堆排序" 实现的，只有弹出出来时才有顺序，直接打印优先队列是无序的
"""
import heapq

pqueue = []
heapq.heappush(pqueue, (1, 'A'))
heapq.heappush(pqueue, (7, 'B'))
heapq.heappush(pqueue, (3, 'C'))
heapq.heappush(pqueue, (6, 'D'))
heapq.heappush(pqueue, (2, 'E'))
# print(pqueue) #无序的，只有一个一个弹出来才是有序的
# print(heapq.heappop(pqueue)) #有序