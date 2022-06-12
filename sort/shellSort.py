"""
希尔排序由 插入排序演化而来
希尔排序( Shell Sort)是一种分组插入排序算法。
首先取一个整数d,=n/2,将元素分为d,个组,每组相邻量元素之间距离为d4,在各组内进行直接插入排序;
取第二个整数d2=d1/2,重复上述分组排序过程,直到dl=1,即所有元素在同一组内进行直接插入排序
希尔排序每趟并不使某些元素有序,而是使整体数据越
来越接近有序;最后一趟排序使得所有数据有序。

"""
import random


def inserSort_gap(li, gap):
    for i in range(gap, len(li)):  # 这里不能-1
        tmp = li[i]  # 抽出的那张牌
        j = i - gap  # 被摸牌左边的第一张的指针
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap  # 继续向左寻找
        # 如果不比左边的大，放在原来的地方li[i]，不后移
        li[j + gap] = tmp  # 因为之前j=i-1 所以现在i=j+1


def shellSort(li):
    d = len(li) // 2
    while d >= 1:
        inserSort_gap(li, d)
        d //= 2

li = list(range(17))
random.shuffle(li)
print(li)
shellSort(li)
print(li)
