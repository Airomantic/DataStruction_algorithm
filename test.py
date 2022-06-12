
# 一元二次方程
a=float(input("请输入a："))
b=float(input("请输入b："))
c=float(input("请输入c："))
dert=b**2-4*a*c
if dert >= 0:
    x1=(-b+dert**0.5)/(2*a)
    x2=(-b-dert**0.5)/(2*a)
    print("x1:",x1)
    print("x2:",x2)
else:
    print("无解")
