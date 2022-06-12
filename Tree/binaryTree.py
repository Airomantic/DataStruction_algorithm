
"""
            E
     A            G
        C            F
      B   D
"""
from collections import deque


class BiTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
"""插入数据"""
a=BiTreeNode("A")
b=BiTreeNode("B")
c=BiTreeNode("C")
d=BiTreeNode("D")
e=BiTreeNode("E")
f=BiTreeNode("F")
g=BiTreeNode("G")

e.left=a
e.right=g
a.right=c
c.left=b
c.right=d
g.right=f
root=e

print(root.left.right.data)

def preOrder(root):
    if root:
        print(root.data,end=",")
        preOrder(root.left)
        preOrder(root.right)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=",")
        inOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=",")
"""层次遍历"""
def levelOrder(root):
    queue=deque() #队列，注意加括号
    queue.append(root) #根先进队
    while len(queue)>0: #只要队不空
        node=queue.popleft()
        print(node.data,end=",") #访问出队这个元素
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# preOrder(root)
levelOrder(root)