"""
完全二叉树:叶节点只能出现在最下层
和次下层,并且最下面一层的结点都集
中在该层最左边的若干位置的二叉树
O(2nlog(n))
"""
import random


def shift(li,low,high):
    """ 大根堆
    :param li:
    :param low:
    :param high:
    :return:
    """
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high: #注意 是j 不是low
        if j + 1 <= high and li[j+1] > li[j]:
            j += 1 #向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heapSort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i 表示建堆时调整部分的根的下标
        shift(li, i, n-1)
    #建堆完成，父节点都大于子结点
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        shift(li, 0, i-1)  #每次换下最大值后都要重新再调整堆为大根堆的构造

li = [i for i  in range(100)]
random.shuffle(li)
print(li)
heapSort(li)
print(li)






