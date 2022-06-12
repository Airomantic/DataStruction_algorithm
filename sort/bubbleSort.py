
"""
一般电脑运行1s的运行效率是10^7次基本操作

列表每两个相邻的数,如果前面比后面大,则交换这两个数
趟排序完成后,则无序区減少ー个数,有序区增加一个数。
代码关键点:趟、无序区范围
"""
# from cal_time import *
# @cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j+1],li[j]=li[j],li[j+1]

def bubble_sort2(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1): #一趟会把最大值移动上去，然后第二大，第三大......
            if li[j]>li[j+1]:
                li[j+1],li[j]=li[j],li[j+1]

#出现已经排好序则无需再继续排序下去了
def bubble_sort3(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        print(li)
        if not exchange:
            return

li=[9, 8, 7, 1, 2, 3, 4, 5, 6]

bubble_sort3(li)
print(li)