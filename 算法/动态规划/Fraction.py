"""
数论：是专门研究整数的，质数
应用： 密码学，加密算法 RSA
"""

class Fraction:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        x=self.gcd(a,b)
        self.a/=x
        self.b/=x

    # @staticmethod #静态方法不要self
    def gcd(self,a, b):
        while b>0:
            r=a%b
            a=b
            b=r
        return a
    """最小公倍数"""
    def LCM(self,a,b):
        #12 16 --> 4
        #3*4*4
        x=self.gcd(a,b)
        return a*b/x
    """+"""
    def __add__(self, other): #1/12 + 1/20 other自带
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        denominator=self.LCM(b,d) #分母
        molecular = a*denominator/b+c*denominator/d #分子
        return Fraction(molecular,denominator)
    """减 除div 乘"""
    def __str__(self):
        return "%d/%d" %(self.a,self.b)

# f=Fraction(30,16) #不加上静态规划也可
# print(f)

a=Fraction(1,3) #1/3
b=Fraction(1,2) #1/2
print(a+b)