"""
栈空表示 没有路
栈不空实现循环
1 栈实现回溯和深度优先
2 队列实现广度优先
3 递归实现回溯
"""
# 注意每行后有个逗号slices 分割
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


def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNone = stack[-1]  # 关键点1
        if curNone[0] == x2 and curNone[1] == y2:
            for p in stack:
                print(p)
            return True  # 注意return 在if控制
        for dir in dirs:
            nextNone = dir(curNone[0], curNone[1])
            if maze[nextNone[0]][nextNone[1]] == 0:  # 注意这个maze[][] 行列
                stack.append(nextNone)  # 对于这个list的栈相当于压入
                maze[nextNone[0]][nextNone[1]] = 2  # 已走过的路标记为2
                break
        else:  # 没有路
            maze[nextNone[0]][nextNone[1]] = 2  # 再往下一步是封路，当前位置是已走过的路，也记得设置为2
            stack.pop()  # 关键点2：弹栈相当于回溯
    else:
        print("无路可走")
        return False

maze_path(1, 1, 10, 10) #注意边界是墙
