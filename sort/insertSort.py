"""
这个tmp 很妙
O(n^2)
"""
def inserSort(li):
    for i in range(len(li)): #这里不能-1
        tmp=li[i] #抽出的那张牌
        j=i-1 #被摸牌左边的第一张的指针
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j-=1 #继续向左寻找
        #如果不比左边的大，放在原来的地方li[i]，不后移
        li[j+1]=tmp #因为之前j=i-1 所以现在i=j+1

li=[3,4,2,1,9,6,5,8,7]
inserSort(li)
print(li)

