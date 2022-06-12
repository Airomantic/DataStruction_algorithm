"""
https://www.bilibili.com/video/BV1dx411S7WR?spm_id_from=333.999.0.0
"""


def printArray(li, n):
    for i in range(n-1): #注意这里是len-1
        print(li[i],end='')
    print()


def swap(li, i, q):
    temp = li[i]
    li[i] = li[q]
    li[q] = temp


def perm(li, p, q):
    if p == q:
        printArray(li, q + 1)
    for i in range(p,q):
        swap(li, p, i)
        perm(li, p+1, q)
        swap(li, p, i)  # 记得还原回来


if __name__ == '__main__':
    li = [1, 2, 3]
    perm(li, 0, len(li))
