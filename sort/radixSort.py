"""
基数排序 桶排序的近亲
按关键字：个位，十位，百位，...
https://www.bilibili.com/video/BV1A54y1D7Kd?from=search&seid=9529818666508687719&spm_id_from=333.337.0.0
从桶的底部逐个抽出
时间复杂度:O(kn) 线性复杂度比快排还要快
空间复杂度:O(k+n) 跟桶排序一样
K表示数字位数 it

基数排序分为高位优先和低位优先,默认是低位优先
高位优先：最后结果是从大到小
低位优先：最后结果是从小到大
"""
import copy

from DataStructures_algorithms.cal_time import cal_time_decoration

import random

def pivot(li, left , right):
    tmp = li[left] #每次移到左边小的值都会被更新
    while left < right:
        while left < right and li[right] >=tmp:
            right-=1
        li[left] = li[right] #把右边比哨兵tmp小的值放到左边指针指向的空位上
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp #注意！ 在递归时，每次循环都要记得把这个tmp放回原处
    return left #最后左指针和右指针碰上了，返回right和left都可作为mid

def _quickSort(li ,left , right):
    if left < right:
        mid=pivot(li,left,right)
        _quickSort(li, mid+1, right)
        _quickSort(li, left, mid - 1)

@cal_time_decoration  #递归函数会每一步都打印，所以写个函数封装它，注意调用时要精确到函数
def quickSort(li):
    _quickSort(li,0,len(li)-1)

@cal_time_decoration
def radixSort(li):
    maxNum = max(li)
    it = 0
    while 10 ** it <= maxNum:
        buckerts = [[] for _ in range(10)]
        for var in li:
            # 987 it=1  987//10 ->98 98%10=8  it=2 987//100 ->9 9%10=9
            digit = (var // (10 ** it)) % 10
            buckerts[digit].append(var)

        li.clear()
        for buc in buckerts: #每一个bucket[i] 是整体多个数回到li，顺序刚好弹栈式
            li.extend(buc)
        # 继续下轮进位再排序 个位 -> 十位 -> 百位 ->...
        it += 1

# li =list(range(1000000)) #这种情况下基数排序是比快排要快的
# random.shuffle(li)
li = list(random.randint(0,10000000) for _ in range(10000)) #10000000在10万及以上位数时，就比快排慢了
li1=copy.deepcopy(li)
li2=copy.deepcopy(li)

quickSort(li1) # nlogn logn=log(2,n)
radixSort(li2) # nlogn k=logn=log(10,n)

#字符串比较是后面加0

#小数比较麻烦