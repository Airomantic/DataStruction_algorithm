"""
只有key，没有value 的是集合set()，key不能重复
https://blog.csdn.net/yohjob/article/details/99958241
直接寻址表：
缺点:
当域U很大时,需要消耗大量内存,很不实际
如果域U很大而实际出现的keV很少,则大量空间被浪费
无法处理关键字不是数字的情况

改进直接寻址表:哈希( Hashing)
1 构建大小为m的寻址表T
2 key为k的元素放到h(k)位置上 ,h(k)哈希函数
3 h(k)是一个函数,其将域U映射到表T[0,1,...,m-1]

哈希表原理 = 直接寻址表 + 哈希函数
哈希表结构 = 数组 + 链表 + 红黑树
解决哈希冲突
1 开放寻址法：如果哈希函数返回的位置已经有值,则可以向后探查新的位置来存储这个值
    线性探查:如果位置被占用,则探查i+1,i+2,
    二次探查:如果位置i被占用,则探查i+1^2,i-1^2,i+2^2,i-2^2
    二度哈希:有n个哈希函数,当使用第1个哈希函数h1发生冲突时,则尝试使用h2,h3,...
2 拉链法
"""


class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    # """迭代器，因为它支持__next__"""
    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):  # 允许传一个list
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    # """哈希表查找，这个参数self实际上就是LinkList的对象lk"""
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # """迭代器，让链表支持for循环"""
    def __iter__(self):
        return self.LinkListIterator(self.head)

    # """__repr__ 打印的时候转化成字符串，这里的self是可迭代的"""
    def __repr__(self):
        return "<<" + ",".join(map(str, self)) + ">>"


# lk = LinkList([1, 2, 3, 4, 5])
# for element in lk:
#     print(element)


# 类似与集合的结构
class HashTable:
    def __init__(self, size=101):
        self.size = size
        # self.T=[None for _ in range(self.size)] #把None改成空拉链
        self.T = [LinkList() for _ in range(self.size)]  # 开垦空间

    # """哈希函数"""
    def h(self, k):
        return k % self.size

    # """先查找到，在插入"""
    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("duplicated insert")
        else:
            self.T[i].append(k)

    # """根据哈希函数查找"""
    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)

print(",".join(map(str,ht.T)))
print(ht.find(102))