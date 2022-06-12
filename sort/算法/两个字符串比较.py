import io
import sys


class Solution:
    def isAngram(self, s, t):
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt

    def isAngram2(self, s, t):
        return sorted(list(s)) == sorted(list(t))  # sorted是创建一个新数组

    def isAngram3(self, s, t):
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1  # 第一次没有健k 就开辟一个给他，并赋予0+1=1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict2 == dict1


def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield lines.strip('\n')

    lines = readlines()
    while True:
        s = next(lines)
        # s = str(s)
        t = next(lines)
        # t = str(t)
        res = Solution().isAngram3(s, t)
        print(res)


if __name__ == '__main__':
    main()
