class Node(object):
    def __init__(self, key, code=0, parent=None, lchild=None, rchild=None):
        self.key = key
        self.code =code
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild

class HuffmanTree(object):
    def __init__(self, root=None):
        self.huffman_tree = []
        self.root = root

    # 找两个key值最小的节点
    def find2node(self, flag):
        mini=[]
        for i in range(len(self.huffman_tree)):
            if i in flag:
                continue
            if len(mini) < 2: # 最少要有两个叶结点
                mini.append(i)
            else:
                if self.huffman_tree[i]

    def build(self, C):
        #flag记录已经合并的结点
        flag = []
        #初始化各关键字key节点
        n = len(C)
        for key in C:
            self.huffman_tree.append(Node(key)) # 将node挂在哈夫曼结构中
        # 构建hufuman，n个值，需要n-1次合并操作
        for i in range(n,2*n -1):
            mini = self.find2node(flag)
            print(str(mini[0])+'\t'+str(mini[1]))
            #合并的节点记录,下次合并不需要考虑
            flag.append(mini[0])
            flag.append(mini[1])
            # 构建新的Node节点，key为两个子节点key相加
            key = self.huffman_tree[mini[0]].



if __name__ == '__main__':
    tree = HuffmanTree()
    C = [5,9,12,13,16,45]
    tree.build(C)
    