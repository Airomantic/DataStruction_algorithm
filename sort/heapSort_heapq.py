

import heapq #q -> queue 优先队列
import random



li= list(range(100))
random.shuffle(li)
print(li)

#建堆
heapq.heapify(li)

for _ in range(len(li)):
    print(heapq.heappop(li),end=',')