
"""
递归：子问题的重复计算
"""
def fibnacci(n): #递归
    if n==1 or n ==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)
# print(fibnacci(100)) #n=100会蹦掉
"""这个非递归可以就是动态规划dp思想=最优子结构=递推式+重复子问题"""
def fibnacci_no_recursion(n):
    f=[0,1,1]
    if n>2:
        for i in range(n-2): #倒数后三位是[...,n-2,n-1,n]
            num=f[-1]+f[-2]
            f.append(num)
    return f[n]
print(fibnacci_no_recursion(100))
