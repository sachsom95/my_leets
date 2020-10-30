class Solution:
    def maxDepth(self, s: str) -> int:
        depth,maximum = 0,0
        for x in s:
            if (x == "("):
                depth+=1
            elif(x == ")"):
                depth-=1
            if (depth > maximum):
                    maximum = depth
        return (maximum)