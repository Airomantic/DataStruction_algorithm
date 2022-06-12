

"""
快速排序
O(n*log(n)) 一层的复杂度是n，一共log(n)层 最坏会出现O(n^2)
模块 包 类
递归最大深度999，很消耗

https://www.bilibili.com/video/BV1XL411g7qF?p=17&spm_id_from=pageDriver
"""
import copy
import random

from DataStructures_algorithms.cal_time import cal_time_decoration


def pivot(li, left , right):
    tmp = li[left] #每次移到左边小的值都会被更新
    while left < right:
        while left < right and li[right] >=tmp: #因为拿的是tmp = li[left]左边的那个数做比较，所以左边留有空位，拿出的数跟最右边的数比较li[right] >=tmp
            right-=1  #while循环目的是要找到不满足条件时会一直循环，我找的是右边小于左边拿出来的tmp数，li[right] < tmp
            # 因为设置的条件是>=，即=时还需要right向左边走一步，所以必须再添加一个条件left<right
        #否则就是li[right] < tmp
        li[left] = li[right] #把右边比哨兵tmp小的值放到左边指针指向的空位上
        while left < right and li[left] <= tmp: #从左边找比tmp大的数，如果当前指针没有找到则右移
            left += 1
        li[right] = li[left]
    li[left] = tmp #注意！ 在递归时，每次循环都要记得把这个tmp放回原处
    return left #最后左指针和右指针碰上了，返回right和left都可作为mid

def _quickSort(li ,left , right):
    if left < right:
        mid=pivot(li,left,right)
        _quickSort(li, mid+1, right)
        _quickSort(li, left, mid - 1)

li=list(range(10000))
random.shuffle(li) #打乱

@cal_time_decoration  #递归函数会每一步都打印，所以写个函数封装它，注意调用时要精确到函数
def quickSort(li):
    _quickSort(li,0,len(li)-1)

#深拷贝相同打乱的数组
li1=copy.deepcopy(li)
li2=copy.deepcopy(li)

quickSort(li)
print(li)