import io
import json
import sys

"""
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
5
O(mn)

0 1 2  3
4 5 6  7
8 9 10 11
i = num//4    j = num%4
"""


def stringToIntegerList(input):
    return json.loads(input)


class Solution:

    def searchMatrix(self, matrix, target):
        for line in matrix:
            if target in line:
                return True
        return False

    def searchMatrix2(self, matrix, target):
        h = len(matrix)
        if not h:
            return False
        w = len(matrix[0])
        if not w:
            return False
        left = 0
        right = h * w - 1
        while left < right:
            mid = (left + right) // 2
            i = mid // h  # 关键点 mid就是个0 1 2 3...的顺序位置
            j = mid % w
            if matrix[i][j] > target:
                right = mid - 1
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                return True
        return False


def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield lines.strip('\n')

    lines = readlines()

    while True:
        matrix = next(lines)
        matrix = stringToIntegerList(matrix)
        target = int(next(lines))
        res = Solution().searchMatrix2(matrix, target)
        print(res)


if __name__ == '__main__':
    main()
