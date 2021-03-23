class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for x in s:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        for x, y in enumerate(s):
            if (dic[y] == 1):
                return x
        else:
            return -1
