"""
桶排序( Bucket Sort):首先将元素分在不同的桶中,在对每个桶中的元素排序。

extend() 把一个list加到另一个list的后面
平均情况时间复杂度:O(n+k)
最坏情况时间复杂度:O(n^2k)
空间复杂度:O(nk)

"""
import random


def buckerSort(li, n=100, maxNum=10000):
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(val // (maxNum // n), n - 1)  # 取min(，n-1) 是防止10000/100=100这种越界情况
        buckets[i].append(val)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sortli = []
    for buc in buckets:
        sortli.extend(buc)
    return sortli

li = [random.randint(0,10000) for i in range(20)]
li = buckerSort(li)
print(li)

