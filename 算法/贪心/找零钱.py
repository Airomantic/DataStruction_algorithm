
"""
贪心：只在当前局部最优解
"""

def change(n):
    t=[100,50,20,5,1] #面值
    m=[0 for _ in range(len(t))]
    for i ,money in enumerate(t):
        m[i]=n//money
        n=n%money
    return m
print(change(376))
