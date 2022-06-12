"""
完全二叉树:叶节点只能出现在最下层
和次下层,并且最下面一层的结点都集
中在该层最左边的若干位置的二叉树
O(2nlog(n))
现在有n个数,设计算法得到前k大的数
"""
import random


def shift(li,low,high):
    """ 小根堆 ：把1 li[j] > li[j+1]和2 tmp > li[j]处的符号设置成大于>
    :param li:
    :param low:
    :param high:
    :return:
    """
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high: #注意 是j 不是low
        if j + 1 <= high and  li[j] > li[j+1]: #1. >
            j += 1 #向右孩子
        if tmp > li[j] : #2.>
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def topK(li,k):
    heap=li[:k]
    #1.建堆 小根堆
    for i in range((k-2)//2, -1, -1):
        shift(heap, i, k-1)

    #2.遍历 看k+1以及后面元素逐个调往堆顶比较，大于堆顶元素heap[0]进入，小于则舍弃
    for i in range(k, len(li)-1):
        if heap[0] < li[i]:
            heap[0] = li[i]
            shift(heap, 0, k-1) #做一次新进元素后的调整
    #3.出数
    for i in range(k-1, -1, -1): #针对排好序的heap[]
        heap[0], heap[i] = heap[i], heap[0] #小根堆，把大放上去
        shift(heap, 0, i-1)
    return heap

def heapSort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i 表示建堆时调整部分的根的下标
        shift(li, i, n-1)
    #到这里 建堆完成，父节点都大于子结点
    """出数"""
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        shift(li, 0, i-1)  #每次换下最大值后都要重新再调整堆为大根堆的构造

li = [i for i  in range(100)]
random.shuffle(li)
print(li)
# heapSort(li)
print(topK(li,10))







