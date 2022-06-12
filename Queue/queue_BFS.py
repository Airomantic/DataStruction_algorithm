"""
https://www.bilibili.com/video/BV1uA411N7c5?p=56&spm_id_from=pageDriver
队列 里面存的是分叉元素的终端
通过另一个数组 记录-哪个元素出队导致终点元素进队的，即倒着找回去

｜ 1 ｜ 2 ｜ 3 ｜ 4 ｜ 5 ｜ 6 ｜ 7 ｜
｜ -1｜ 0 ｜ 1 ｜ 2 ｜ 2 ｜ 3 ｜ 4 ｜
1 <- 2 <- 3 <- 5 <- 7
"""
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# ()元组 上下左右
dirs = [
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y)
]


def print_r(path):
    curNone = path[-1]  # 最后元素就是终点，注意curNode是二维3列的，curNone[2]记录着所处的位置
    realpath = []  # 二维2列
    while curNone[2] == -1:
        realpath.append(curNone[0:2])  # 即 0 1
        curNone = path[curNone[2]]  # 找下一个节点，
    realpath.append(curNone[0:2])  # 把起点放进去
    # 因为先append终点，然后append终点的前一个点，然后再前一个点，再前一个点...
    realpath.reverse()  # 这是个列表
    for node in realpath:
        print(node)

def maze_BFS_queue(x1, y1, x2, y2):
    # 三维 还需要保存下标是哪个元素让它进队的
    queue = deque()
    queue.append((x1, y1, -1))  # 进队，起点是-1这个下标让它进队的\
    path = []
    while len(queue) > 0:
        curNone = queue.pop()  # 队尾出队
        path.append(curNone)
        if curNone[0] == x2 and curNone[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNone = dir(curNone[0], curNone[1])
            if maze[nextNone[0]][nextNone[1]] == 0:
                # path[curNone]下标len(path) - 1 的出队导致（nextNone[0], nextNone[1]）的进队
                queue.append((nextNone[0], nextNone[1], len(path) - 1))
                maze[nextNone[0]][nextNone[1]] = 2
                # 没有break 因为广度优先是多个方向同时找的，没有栈的回溯性
    else:
        print("没有路！")
        return False


maze_BFS_queue(1, 1, 10, 10)
