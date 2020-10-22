class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        lst = []
        for x,y in enumerate(nums):
            sum += y
            lst.append(sum)
        return lst
            

