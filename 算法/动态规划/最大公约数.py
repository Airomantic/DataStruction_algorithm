"""
https://www.bilibili.com/video/BV1uA411N7c5?p=95
应用：
欧几里得算法，实现 分数的四则运算
"""

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b) #这是个伪递归跟循环一样
print(gcd(12,16))

def gcd_no_recurs(a,b): #记住那个方块动画就很容易理解了
    while b>0:
        r=a%b
        a=b #当假设r=0时，公约数就是a=b，即a
        b=r
    return a

print(gcd_no_recurs(12,16))