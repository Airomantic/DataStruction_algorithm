"""
假设现在的列表分两段有序,如何将其合成为一个有序列表
归并算法很有用，python内置的sort()就是归并的原理 Timsort()
"""


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    litmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            litmp.append(li[i])
            i += 1
        else:
            litmp.append(li[j])
            j += 1
    #这一段是：当一边全都满足小于或大于另外一边时，不用再比较直接逐个全部插入排序数组后面
    while i <= mid:
        litmp.append(li[i])
        i += 1
    while j <= high:
        litmp.append(li[j])
        j += 1
    # 写回去
    li[low:high + 1] = litmp  # ow:high+1 是因为等下还要有递归

li = [2, 4, 5, 7, 1, 3, 6, 8] # 本身是从2 4 5 7和1 3 6 8分开排好的两个升序序列
merge(li, 0, 3, 7)
print(li)
