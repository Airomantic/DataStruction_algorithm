"""
高度平衡树
balance factor
1 根左右子树高度之差不超过1
2 其每个结点的子树继续构成平衡
https://visualgo.net/en/bst?slide=1
https://www.bilibili.com/video/BV1uA411N7c5?p=76&spm_id_from=pageDriver
插入      左逆右顺
右右-左
左左-右
右左-右左
左右-左右

named after inventors Adelson-Velsky and Landis 用于搜索不那么频繁，插入删除更频繁的
"""
from bst import BiTreeNode, BST  # BiTreeNode,BST是bst.py 下的两个类


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        # 多一个数据域
        self.bf = 0  # bf 为balance factor ，以下是：bf = 右 - 左 ，即左偏：-1 右偏：+1


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    """目前仅限于插入，删除还需修改"""

    # 左旋
    def rotate_left(self, p, c):
        s2 = c.left  # 指插入位置
        p.right = s2
        if s2:
            s2.parent = p
        c.left = p
        p.parent = c
        # 每次变动都要更新一下
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.right  # 指插入位置
        p.left = s2
        if s2:  # 反着链接回去需要判断是否为空
            s2.parent = p

        c.right = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c  # c取代了p

    def rotate_right_left(self, p, c):
        g = c.left  # 定义为对根结点右支上的左支的孩子结点进行插入

        s3 = g.right  # 先假设插入的结点在g右支上
        c.left = s3
        if s3:
            s3.parent = c
        g.right = c
        c.parent = g

        s2 = g.left  # 后假设插入的结点在g左支上
        p.right = s2
        if s2:
            s2.parent = p
        g.left = p
        p.parent = g
        # 一开始p的左支s1=h和c的右支s4=h，而g的左右s2=s3=h-1
        if g.bf > 0:  # 插入的是g的右支上，所以右>左，bf=右-左>0
            p.bf = -1  # p的左支h>g的左支h-1
            c.bf = 0  # c的右左插入了结点，所以右旋后平衡
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        return g  # g替换掉了p，所以返回g

    def rotate_left_right(self, p, c):
        g = c.right
        s2 = g.left
        c.right = s2
        if s2:
            s2.parent = c
        g.left = c
        c.parent = g

        s3 = g.right
        p.left = s3
        if s3:
            s3.parent = p
        g.right = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g  # g替换掉了p，所以返回g

    def insert_no_recursion(self, value):
        # 1 和BST 一样，插入
        p = self.root
        if not p:  # 空树特殊处理
            self.root = BiTreeNode(value)
            return
        while True:
            if value < p.data:
                if p.left:  # 如果说p的左子树不是null，需要继续往左子树走一下
                    p = p.left
                else:  # 左孩子不存在，直接插入
                    p.left = BiTreeNode(value)  # 插入左孩子的位置
                    p.left.parent = p  # 双向的值，还需记得指向父结点
                    node = p.left  # node 存储的就是插入的结点
                    break
            elif value > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTreeNode(value)  # 插入右孩子的位置
                    p.right.parent = p
                    node = p.right
                    break
            else:  # 表示已经有这样一个结点了 val == p.data
                return  # 同样的元素不准插入

            # 2 更新balance factor，沿着树支路径，左分枝的插入结点，bf就-1，右分枝+1，满足bf=右-左
        while node.parent:  # 相当于一个指针指着加入结点的上一级，保证node的父结点不为空
            if node.parent.left == node:
                # 更新node.parent 的 bf -= 1 ，原来的情况只有-1 0 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1 ，更新后变成(-1)-1 = -2
                    # 做旋转
                    # 看node哪边沉 左右-左右
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf > 0:  # 说明右边沉
                        n = self.rotate_left_right(node.parent, node)  # 返回一个结点构成新结点
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得： 把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf == 1 ，更新后变成(1)-1 = 0
                    node.parent.bf = 0  # 一旦一个结点的balance factor变成0就不再传递bf变动了，循环也就不用再传递了
                    break
                else:  # 原来node.parent.bf == 0 ，更新后变成-1
                    # 需要向上传递，但不要旋转
                    node.parent.bf = -1
                    node = node.parent  # 向上继续
                    continue
            else:  # 传递是右子树来的，右子树更沉了
                # 更新node.parent 的 bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1 ，更新后变成(1)+1 = 2
                    # 做旋转
                    # 看node哪边沉 右左-右左 ,node.parent.bf > 0指右， node.bf <0 指左
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf < 0:  # node.bf= -1
                        n = self.rotate_right_left(node.parent, node)
                    else:  ##node.bf=1 一直bf>0 即 右右-左 则左旋
                        n = self.rotate_left(node.parent, node)
                    # 记得： 把n和g连起来
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf == 0 ，更新后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = 0
            if g:
                if node.parent == g.left:  # 原来node是g的左右孩子
                    g.left = n
                else:
                    g.right = n
                break
            else:
                self.root = n
                break


avl = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
avl.preOrder(avl.root)
print()
avl.inOrder(avl.root)
