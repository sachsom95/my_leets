class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index = 0
        lst =['']*len(s)
        for x in indices:
            lst[x] = s[index]
            index+=1
        return ''.join(lst)