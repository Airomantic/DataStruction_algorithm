

"""
B 树（Balance Tree）
https://blog.csdn.net/BGoodHabit/article/details/106209785
https://github.com/Tina-ZJ/Basic_Algorithms/blob/master/BTree.py
https://mp.weixin.qq.com/s/MolVZjVAIXRj48_SreN4MA
https://blog.csdn.net/weixin_34132768/article/details/86196515?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0.no_search_link&spm=1001.2101.3001.4242
规律：
1 在一棵树中检查任意一个节点都需要一次磁盘访问，所以B树避免了大量的磁盘访问
2 一个满的节点y有2t − 1个关键字）按其中关键字y.key_t分裂为两个各含t-1个关键字节点
3 分裂是树长高的唯一途径

MySQL 好处： 磁盘快存储更多数据对应单个节点可以存储多个键值key和数据data的平衡树（每个节点称为页=磁盘快）
①B+ 树非叶子节点上是不存储数据的，仅存储键值，而 B 树节点中不仅存储键值，也会存储数据
B+ 树的阶数是等于键值的数量的，如果我们的 B+ 树一个节点可以存储 1000 个键值，那么 3 层 B+ 树可以存储 1000×1000×1000=10 亿个数据。
一般根节点是常驻内存的，所以一般我们查找 10 亿数据，只需要 2 次磁盘 IO，因为不用算根结点这一层(3-1)
页 1 已经在内存中了，此时不需要到磁盘中读取数据，直接从内存中读取即可，不在内存的需要从磁盘IO到内存
②因为 B+ 树索引的所有数据均存储在叶子节点，而且数据是按照顺序排列的
那么 B+ 树使得范围查找，排序查找，分组查找以及去重查找变得异常简单。而 B 树因为数据分散在各个节点，要实现这一点是很不容易的
"""
# -*- coding:utf8 -*-
import sys


#构造节点
class Node(object):
    def __init__(self, n=0,isleaf = True):
        #节点关键字数量n
        self.n = n
        #关键字keys值
        self.keys = []
        # 孩子节点
        self.childs = []
        #是否是叶子节点
        self.leaf = isleaf
    @classmethod
    def allocate_node(self, key_max):
        node = Node()
        child_max = key_max+1
        #初始化key and child
        for i in range(key_max):
            node.keys.append(None)
        for i in range(child_max):
            node.childs.append(None)
        return node


class BTree(object):
    def __init__(self, t, root=None):
        # B数的最小度数
        self.t = t
        #节点包含的关键字的最大个数
        self.max_key = 2*self.t-1
        #节点包含的最大孩子个数
        self.max_child = self.max_key+1
        #跟节点
        self.root = root

    '''
       输入一个非满的内部节点x，和一个使x.child[i]为x的满子节点的下标i
       把子节点分裂成两个，并调整x
    '''
    def btree_split_child(self, x, i):
        #分配一个新节点
        #z = Node()
        z = self.__new_node()
        #获取x的第i个孩子节点
        y = x.childs[i]
        #更新新生成的节点z
        z.leaf = y.leaf
        #分裂, y关键字2t-1变成t-1，z获取y中最右边的t-1个关键字
        z.n = self.t-1
        #把y的t-1个关键字以及相应的t个孩子赋值z
        for j in range(self.t-1):
            z.keys[j] = y.keys[j+self.t]
        if not y.leaf:
            for j in range(self.t):
                z.childs[j] = y.childs[j+self.t]

        #调整y的关键字个数
        y.n = self.t - 1
        # z插入为x的一个孩子
        for j in range(x.n+1, i, -1):
            x.childs[j] = x.childs[j-1]
        x.childs[i+1] = z
        #提升y的中间关键字到x来分割y和z
        for j in range(x.n, i-1, -1):
            x.keys[j] = x.keys[j-1]
        x.keys[i] = y.keys[self.t-1]
        #调整x的关键字个数
        x.n = x.n+1

    '''
    将关键字k插入到节点x中，假定在调用过程中x是非满的
    '''
    def btree_insert_nonfull(self, x, k):
        i = x.n
        #x是叶子节点，直接插入
        if x.leaf:
            while i>=1 and k<x.keys[i-1]:
                x.keys[i] = x.keys[i-1]
                i-=1
            x.keys[i] = k
            #更新节点数
            x.n+=1
        #非叶节点
        else:
            while i>=1 and k<x.keys[i-1]:
                i-=1
            i+=1
            #判断是否递归降至一个满子节点
            if x.childs[i-1].n == 2*self.t-1:
                self.btree_split_child(x,i-1)
                #确定向两个孩子中哪个下降是正确的
                if k>x.keys[i-1]:
                    i+=1
            #递归地将k插入合适的子树中
            self.btree_insert_nonfull(x.childs[i-1],k)
    def __new_node(self):
        '''
        创建新的B树节点
        '''
        return Node().allocate_node(self.max_key)
    '''
    插入，利用btree_insert_child保证递归始终不会降至一个满节点
    '''
    def btree_insert(self, k):
        # 检查是否为空树
        if self.root is None:
            node = self.__new_node()
            self.root = node
        r = self.root
        #根节点是满节点
        if r.n == 2*self.t - 1:
            #s = Node()
            s = self.__new_node()
            # s成为新的根节点
            self.root = s
            s.leaf = False
            s.n = 0
            s.childs[0] = r
            #分裂根节点，对根进行分裂是增加b树高度的唯一途径
            self.btree_split_child(s,0)
            self.btree_insert_nonfull(s,k)
        else:
            self.btree_insert_nonfull(r,k)

    #遍历,逐层遍历
    def btree_walk(self):
        current = [self.root]
        while current:
            next_current = []
            output = ""
            for node in current:
                if node !=None and node.childs:
                    next_current.extend(node.childs)
                if node !=None:
                    output+=''.join(node.keys[0:node.n]) + " "
            print(output)
            current = next_current

    #中序遍历，从小到大的顺序输出key
    def btree_order(self, tree):
        if tree is not None:
            for i in range(tree.n):
                self.btree_order(tree.childs[i])
                print(tree.keys[i],end=" ")
                self.btree_order(tree.childs[i+1])
    # search
    def btree_search(self,x, k):
        i = 0
        while i<=x.n and k > x.keys[i]:
            i+=1
        # 检查是否已经找到关键字
        if i < x.n and k == x.keys[i]:
            return (x,i)
        #没找到，若是叶子节点，则查找不成功
        elif x.leaf:
            return None
        #非叶子节点，继续递归查找孩子节点
        else:
            return self.btree_search(x.childs[i],k)

if __name__=='__main__':
    tree = BTree(3)
    for x in ['G','M','P','X', 'A','C','D','E','J','K','N','O','R','S','T','U','V','Y','Z', 'B','Q','L', 'F']:
        tree.btree_insert(x)
    #逐层遍历和从小到大遍历输出z
    tree.btree_walk()
    tree.btree_order(tree.root)
    print('\n')
    #search
    result = tree.btree_search(tree.root, '1')
    if result!=None:
        print("find key :"+result[0].keys[result[1]])
    else:
        print("not find key")

