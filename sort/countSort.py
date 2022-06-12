"""
计数排序
列表中的数范围都在0到100之间 注意0-100整型 类型有限
"""
from DataStructures_algorithms.cal_time import cal_time_decoration


@cal_time_decoration
def countSort(li, maxCount=100):
    count = [0 for _ in range(maxCount + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for index,val in enumerate(count):
        for i in range(val):
            li.append(index)

@cal_time_decoration
def sys_sort(li):
    li.sort() #C++

import random,copy
li =[random.randint(0,100) for _ in range(10000000)]

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

countSort(li1)
sys_sort(li2)


