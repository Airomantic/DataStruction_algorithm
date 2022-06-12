"""
贪心：只在当前局部最优解
0-1背包 不太适合
分数背包
"""


def fractions_backpack(w):
    goods=[(60,10),(100,20),(120,30)]#元组
    goods.sort(key=lambda x:x[0]/x[1],reverse=True)
    total_p=0
    num=[0 for _ in range(len(goods))]
    for i ,(price,weight) in enumerate(goods):

        if w>=weight:
            num[i]=1 #通过循环一次一次从大到小比较来加入对应的价值下标
            total_p+=price
            w-=weight
        else:
            num[i]=w/weight #剩下的w比weight小
            total_p+=price*num[i]
            # break #可以写下跳出
    return num,total_p

print(fractions_backpack(50))


