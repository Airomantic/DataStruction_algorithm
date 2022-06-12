
"""
Binary Search Tree (BST)二叉搜索树  之后的 AVL红黑树（出现重复数据结点）
两个下划线__的函数表示私有的，在类里面用就行了
"""
import random

class BiTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None #加上就是双链表


class BST:
    def __init__(self,lis=None):
        self.root=None #构造函数创建一个根结点
        """传一个list进来"""
        if lis:
            for value in lis:
                self.insert_no_recursion(value)
    """递归，有参数node"""
    def insert(self,node,value): #这个node表示递归插到哪个结点
        if not node:
            node=BiTreeNode(value) #最后记得return node
        elif value<node.data:
            node.left=self.insert(node.left,value) #递归
            node.left.parent=node #他的左孩子的父亲给他自己，构成双链表
        elif value>node.data:
            node.right = self.insert(node.right, value)  # 递归
            node.right.parent = node
        return node
    """非递归插入 非递归没有参数node"""
    def insert_no_recursion(self,value): #非递归没有参数node
        p=self.root
        if not p: #空树特殊处理
            self.root=BiTreeNode(value)
            return
        while True:
            if value<p.data:
                if p.left: #如果说p的左子树不是null，需要继续往左子树走一下
                    p=p.left
                else: #最孩子不存在，直接插入
                    p.left=BiTreeNode(value)
                    p.left.parent=p #双向的值，还需记得指向父结点
                    return
            elif value>p.data:
                if p.right:
                    p=p.right
                else:
                    p.right=BiTreeNode(value)
                    p.right.parent=p
                    return
            else:
                return
    """递归查询"""
    def query(self,node,value):
        if not node:
            return None
        if node.data<value:
            return self.query(node.right,value)
        elif node.data>value:
            return self.query(node.left, value)
        else:
            return node #成功找到
    """非递归查询"""
    def query_no_recursion(self,value):
        p=self.root
        while p:
            if p.data<value:
                p=p.right
            elif p.data>value:
                p=p.left
            else:
                return p
        return None
    """删除"""
    def __remove_node_1(self,node):
        #case1 : node是叶子结点
        if not node.parent: #只有根的父结点是空，说明树里就只有这一个结点
            self.root=None # 置为空就行
        #平行父子关系
        if node == node.parent.left: #node是它父亲的左孩子
            node.parent.left=None #父子断连
            # node.parent=None
        else: #右孩子
            node.parent.right=None
    def __remove_node_21(self,node):
        #case2 : node只有一个左孩子
        if not node.parent: #根结点
            #（根只有一个孩子）他的左孩子成为新的根
            self.root=node.left
            node.left.parent=None #左孩子现在是根里，它的父结点就有置为空
        elif node ==node.parent.left: #接下来就是链表删除（跳过连接）很简单
            node.parent.left=node.left
            node.left.parent=node.parent #上移指针替换
        else:
            node.parent.right=node.right
            node.right.parent=node.parent
    def __remove_node_22(self,node):
        if not node.parent: #每次都先判断他是不是根结点
            self.root=node.right
        elif node==node.parent.left:
            node.parent.left=node.right
            node.right.parent=node.parent
        else:
            node==node.parent.right
            node.parent.right=node.right #注意node.left
            node.right.parent=node.parent
    def delete(self,value):
        """先找到该结点才能删掉"""
        if self.root: #不是空树
            node=self.query_no_recursion(value)
            if not node: #不存在要想删除的结点
                return False
            """接下来三种case"""
            if not node.left and not node.right: #1 叶子结点
                self.__remove_node_1(node)
            elif not node.right:#21 只有一个孩子（只有一个左孩子）
                self.__remove_node_21(node)
            elif not node.left: #22 只有一个孩子（只有一个右孩子）
                self.__remove_node_22(node)
            else: #3.两个孩子都有
                #先找右子树最小的结点
                min_node=node.right
                while min_node.left:
                    min_node=min_node.left
                node.data=min_node.data#上移替换
                #删除  #要么是叶子结点，要么是只有一个右孩子结点
                if min_node.right:
                    self.__remove_node_22(node)
                else: #没有右孩子就是只有叶子结点
                    self.__remove_node_1(min_node)


    """遍历"""
    def preOrder(self,root):
        if root:
            print(root.data,end=",")
            self.preOrder(root.left)
            self.preOrder(root.right)
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=",")
            self.inOrder(root.right)
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=",")
# test1_lis=[4,6,7,9,2,1,3,5,8]
# test2_lis=list(range(100))
# test3_lis=list(range(0,500,2))
# random.shuffle(test3_lis)

# tree.preOrder(tree.root)
# print("")
# tree.inOrder(tree.root) #刚好排好序，因为左<根<右 跟BST的规则一样
# print("")
# tree.postOrder(tree.root)

# tree=BST(test3_lis)
# print(tree.query_no_recursion(4).data)

test1_lis=[4,6,7,9,2,1,3,5,8]
tree=BST(test1_lis)
tree.inOrder(tree.root)
print("")
tree.delete(4)
tree.delete(1)
tree.delete(8)
tree.inOrder(tree.root)
