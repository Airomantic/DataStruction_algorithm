
"""
文件系统索引
"""
class TreeNode:
    def __init__(self,name,type='dir'):
        self.name=name
        self.type=type #"dir" or "file"
        self.children=[] #往下找
        self.parent=None #只往上找一位，不要弄成数组
        #链式存储
        
    """打印出name需要repr函数"""
    def __repr__(self):
        return self.name
# n=TreeNode('hello')
# n2=TreeNode('world')
# n.children.append(n2)
# n2.parent=n

class FileSystemTree:
    def __init__(self):
        self.root=TreeNode("/")
        self.now=self.root

    def mkdir(self,name):
        #name以/结尾
        if name[-1]!="/":
            name+="/"
        treeNode=TreeNode(name)
        self.now.children.append(treeNode)
        treeNode.parent=self.now
    """展示当前文件下的索引目录"""
    def ls(self):
        return self.now.children #当前目录的children

    """切换目录"""
    def cd(self,name):
        #相对路径，从当前目录往下找
        if name[-1]!="/":
            name+="/"
        """支持向上返回一级"""
        if name=="../":
            self.now=self.now.parent
            return
        for child in self.now.children:
            if child.name==name: #如果等于传进来的name
                self.now=child #切换目录
                return #结束了，不要再往后搜索了
        raise ValueError("如果没有 invalid name")

tree=FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
# print(tree.root.children)

tree.cd("bin/")
tree.mkdir("python/")

tree.cd("../")

print(tree.ls()) #注意ls()函数有括号