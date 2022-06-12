

"""
cmp 在python2当中可以对数组元素进行比较，返回1,0,-1

"""
from functools import cmp_to_key

li=[32,94,128,1286,6,71]

def xy_cmp(x,y):
    if x+y < y+x: #后者写出y+x，而不是x+y
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(li):
    li=list(map(str,li)) #转化成字符
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)

print(number_join(li))

