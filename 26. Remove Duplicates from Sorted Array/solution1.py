class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for x in range(len(nums)):
            if(nums[index]!= nums[x]):
                index+=1
                nums[index] = nums[x]
        return index+1
