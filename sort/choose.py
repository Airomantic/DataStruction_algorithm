
"""
算法关键点: 有序区和无序区、无序区最小数的位置
"""
def select_sort(li):
    for i in range(len(li)-1): #和冒泡一样，剩下最后一个一定是最大的
        min_dex=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_dex]:
                min_dex= j
        if min_dex !=i: #也可不用这个if
            li[i],li[min_dex]=li[min_dex],li[i],
        print(li)

li=[3,4,2,1,9,6,5,8,7]
select_sort(li)
print(li)