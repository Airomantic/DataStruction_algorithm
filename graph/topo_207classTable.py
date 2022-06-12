"""
https://leetcode-cn.com/problems/course-schedule/
指向一个结点的箭头数目：in_degrees
如果不断去掉in_degrees=0的结点，可以最终把整张图都去掉的话，那说明图中没有环，即课可以上完
如果出现带环的情况，现在虽然可以先上0这门课，但上完0这门课之后，没有一个结点的in_degrees是0，最终就留下了一个环状物，整张图没有被消灭掉
一般构建图的方法有2种：
1 数据比较复杂，使用一个class来构建图，每一个object of class是图上的一个node
2 数据简单integer，课程代号，则使用dict of list

https://leetcode-cn.com/problems/course-schedule-ii/
看视频讲解： https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
"""
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites:list[list[int]]):
        # build graph:dict of list
        ## build node
        nodes = dict()
        for n in range(numCourses): # 初始化，建立所有可能的key，并且赋一个初始值(空集)
            nodes[n] = [] # 所有可能的key都定义出来
        ## build edge [i,j] i<-j 遍历prererequisites，key是第二个数
        for e in prerequisites:
            nodes[e[1]].append(e[0])
        """构建完成"""
        # topoSort 本质上是BFS
        ## find indegrees
        indegree = dict()##因为和in_degree有关，所有构建一个diction来保存in_degrees
        for n in range(numCourses):
            indegree[n] = 0
        for e in prerequisites:
            indegree[e[0]] += 1

        ## BFS
        ### init queue
        q = deque # 定义一个Queue
        # 把indegree=0的node都放进Queue
        for k in indegree.keys():
            if indegree[k] == 0:
                q.append(k)
        ### while loop
        n_taken = 0 #计数器
        # BFS的while loop条件一般是Queue不为空
        while q:
            # pop出node
            cur = q.popleft()
            # service 从这个图中消灭完这个node,但由于这个node之后也不会被访问，所以只需消灭它的edge，service可暂时空着不写
            n_taken +=1
            # 把这门课加在计数器上
            # 对children操作，并且把有潜力的child放进queue 一个node可能有多个children，采用for循环
            for child in nodes[cur]: #由于当前node消失了，它的所有child的in_degrees减1
                indegree[child] -=1
                if indegree[child] == 0:
                    q.append(child)

            # 如果这个BFS循环可以遍历全部的node，那么说明这个图上没有环形，可以用这个信息来做个dztion
            # 怎样知道BFS有没有遍历全部的node呢？ 计数器：每pop一个node，就上了一门课，就在计数器上加1，如果退出BFS循环，计数器里面上过的课程数目等于给定的课程数目，那说明图上没有环状物
        #decide # 把计数器和总课程相比
        if n_taken == numCourses:
            return True
        else:
            return False
