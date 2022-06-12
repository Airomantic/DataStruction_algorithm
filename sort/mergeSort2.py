"""
假设现在的列表分两段有序,如何将其合成为一个有序列表
归并算法很有用，python内置的sort()不是归并但是基于归并排序的，它用的是Timsort
https://blog.csdn.net/u010883226/article/details/84403263
快速排序 < 归并排序 < 堆排序
分解:将列表越分越小,直至分成一个元素。
终止条件:一个元素是有序的。
合并:将两个有序列表归并,列表越来越大。
        10    4    6    3    8    2    5    7
     10   4   6   3             8   2   5   7
    10  4     6  3              8  2     5  7
   10      4 6          3  8        2 5      7
      4  10     3  6         2  8      5  7
    3 4 6 10                2 5 7 8
              2345678 10
时间复杂度：O(n*log(n))
空间： O(n)
只要是递归也会有空间复杂度是O(log n)
"""

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    litmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            litmp.append(li[i])
            i += 1
        else:
            litmp.append(li[j])
            j += 1

    while i <= mid:
        litmp.append(li[i])
        i += 1
    while j <= high:
        litmp.append(li[j])
        j += 1
    # 写回去
    li[low:high + 1] = litmp  # ow:high+1 是因为等下还要有递归


# li = [2,4,5,7,1,3,6,8]
# merge(li,0,3,7)
# print(li)

def mergeSort(li, low, high):
    if low < high:  # 至少有两个元素，递归，即当low和high差不多相等时，分解就是0 或1
        # 递归归并排序左边 -> 递归归并排序右边 -> 把左右两边进行归并排序（不递归）
        mid = (low + high) // 2
        mergeSort(li, low, mid)
        mergeSort(li, mid + 1, high)
        merge(li, low, mid, high)

def mergeSort_test(li, low, high):
    if low < high:  # 至少有两个元素，递归，即当low和high差不多相等时，分解就是0 或1
        # 递归归并排序左边 -> 递归归并排序右边 -> 把左右两边进行归并排序（不递归）
        mid = (low + high) // 2
        mergeSort_test(li, low, mid)
        mergeSort_test(li, mid + 1, high) #这两个的顺序归并的块是大到小的
        # merge(li, low, mid, high)
        print(li[low:high+1])

li=list(range(17))
import random
random.shuffle(li)
mergeSort_test(li,0,len(li)-1)
print(li)