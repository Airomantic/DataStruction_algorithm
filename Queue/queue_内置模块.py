"""
双向队列：队首队尾都能出队进队
queue 也是队列，是保证线程安全的，做一些算法的工作就不要用它
collections 里面包含了很多数据结构如dict，dequeue
"""
from collections import deque

q = deque([1, 2, 3, 4, 5], 5)
"""只用这两个就是单向队列"""
q.append(6) #队尾进队，把对头的元素1挤出去
q.append(7) #挤出去2
print(q.popleft()) #队首3出队

"""用于双向队列"""
q.appendleft(1) #队首进队
print(q.pop()) #队尾出队

def tail(n):
    with open('testData', 'r') as f:
        q = deque(f,n)
        return q

for line in tail(5):
    print(line,end=',')