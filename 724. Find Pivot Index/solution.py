class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = 0
        for x in nums:
            sum_right += x

        left = 0
        for x in range(len(nums)):
            if(left == sum_right - nums[x] - left):
                return x
            left += nums[x]
        return -1
