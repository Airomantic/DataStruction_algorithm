"""
最长公共子序列
应用场景： 1 字符串相似度比对 模糊搜索  2 基因🧬比对 ATCG
穷举：O(2^n)
问题：要求a=" ABCBDAB"与b=" BDCABA"的LCS:
由于最后一位"B"≠"A"：
    因此LCS(a,b)应该来源于LCS(a[:-1],b)与LCS(a,b[:-1])中更大的那一个
       =    0
c[i][j]= c[i-1][j-1]+1
       = max(c[i-1][j],c[i][j-1])
"""
def LCS_length(x,y):
    m,n=len(x),len(y)
    c=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]: #i j 一行先一个字符和另一串字符比较
                c[i][j]=c[i-1][j-1]+1 #一行一行计算
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])

    for _ in c: #记录的表格，c是二维
        print(_)
    return c[m][n]

# print(LCS_length("ABCBDAB","BDCABA"))
def LCS(x,y):
    m,n=len(x),len(y)
    c=[[0 for _ in range(n+1)] for _ in range(m+1)]
    b=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]: #i j 左上方
                c[i][j]=c[i-1][j-1]+1 #一行一行计算
                b[i][j]=1 #'↖️'
            elif c[i-1][j]>c[i][j-1]: #上方的大于左方的，说明刚才变化的是来自上方 ，在这里改成>=就是BCAB了
                c[i][j]=c[i-1][j]
                b[i][j]=2 #'⬆️'
            else:
                c[i][j]=c[i][j-1]
                b[i][j]=3 #'⬅️'
    return c[m][n],b #动态规划最优值和动态规划过程（方向）需要记录一下

def lcs_trackback(x,y):
    c,b=LCS(x,y)
    i,j=len(x),len(y)
    res=[]
    while i>0 and j>0:
        if b[i][j]==1: #左上方匹配，记录📝
            res.append(x[i-1])
            i-=1
            j-=1
        elif b[i][j]==2: #不匹配继续向上回退
            i-=1
        else: #不匹配继续向左回退
            j-=1
    return "".join(reversed(res)) #倒着记录的需要反转回来
print(lcs_trackback("ABCBDAB","BDCABA")) #BDAB和BCAB 都是最大公共子序列