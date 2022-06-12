
"""
前面两个是递归
动态规划dp思想=最优子结构=递推式+重复子问题
长度i    | 0   1   2   3   4   5   6   7   8   9   10
价格p(i) | 0   1   5   8   9  10   17  17  20  24  30
r(i)    | 0   1   5   8   10  13  17  18  22  25  30
s(i)    | 0   1   2   3   2   2   6   1   2   3   10
"""

#计算时间
import time

def cal_time(fuc):
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=fuc(*args,**kwargs) #注意要对应好
        t2=time.time()
        print("%s running time: %s secs."%(fuc.__name__,t2-t1))
        return result
    return wrapper

p=[0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40]
p2=[0,1,5,8,9,10,17,17,20,24,30]

"""
r(n)=max(pn,r1+r(n-1),r2+r(n-2),...,r(n-1)+r1)
缺点：重复计算一半的值
"""
def cut_rod_recurision_1(p, n):
    if n==0:
        return 0
    else:
        r_n=p[n]
        for i in range(1,n): #因为下标0即第一个为r_n=p[n]，要从第二个下标1开始
            r_n=max(r_n, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n - i))
        return r_n
#你各一个递归它就用递归装饰，所以需要再套一层
@cal_time
def c1(p,n):
    return cut_rod_recurision_1(p,n)

"""
自顶向下递归实现  时间复杂度2^n爆炸💥级别 递归算法是由于重复求解相同的子问题，效率极低
简化递推式: r(n)=max(p(n)+r(n-i))  1<=i<=n
继续对右边的r(n-1)...r(2),r(1)一刀切割，即把r(n-1)用p(n-1)替换，如r(n-i)=p(n-i)这里用递归就可以了
左边不切割，右边切割
"""
def cut_rod_recurision_2(p,n): #这个函数就是求r_n=res
    if n==0:
        return 0
    else:
        res=0 #都是正的 r_n=res
        for i in range(1,n+1): #1<=i<=n
            res=max(res,p[i]+cut_rod_recurision_2(p,n-i))
        return res
@cal_time
def c2(p,n):
    return cut_rod_recurision_2(p,n)

# print(cut_rod_recurision_1(p, 9))
# print(c1(p,20)) #很慢
# print(c1(p,10))
# print(c2(p,10))

"""
不重复求解，存到列表里，自底向上算
动态规划的思想：
1 每个子问题只求解一次，保存求解结果
2 之后需要此问题，只需查找保存的结果
仍是： r(n)=max(p(n)+r(n-i))  1<=i<=n
时间复杂度：O(n^2)
每次取这个前一步计算好的r()值，而不是重新算一遍
"""
@cal_time
def cut_mod_dp(p,n):
    r=[0]
    for i in range(1,n+1): #循环n此，也可以写成(n)，对于r[i-j]这样就实现了i代替n，j代替i
        res=0
        for j in range(1,i+1):
            res=max(res,p[j]+r[i-j]) #取出保存的值r[i-j]，对于p[i]，需j代替n(i代替n，j由代替了i)
        r.append(res)  #res是i这个值，保存到r[]，也可以写成 r[i]=res
    return r[n]

# print(cut_mod_dp(p,20))

"""
动态规划——重构解
切割方案
"""
def cut_mod_extend(p,n):
    r=[0]
    s=[0]
    for i in range(1,n+1):
        res_r=0 #价格最大值
        res_s=0 #价格最大值对应最优切割方案的左边不切割部分
        for j in range(1,i+1):
            if p[j]+r[i-j]>res_r:
                res_r=p[j]+r[i-j]
                res_s=j
        r.append(res_r)
        s.append(res_s)
    return r[n],s  #最大价格，所有最优切割方案表

def cut_mod_solution(p,n):
    r,s=cut_mod_extend(p,n)
    ans=[]
    while n>0:
        ans.append(s[n])
        n-=s[n]
    return ans #对应目标长度的详细切割方案

print(cut_mod_solution(p2,9))
print(cut_mod_extend(p,20)[0],cut_mod_solution(p,20)) #找到原始表检查 maxPrice=5+17*3=56