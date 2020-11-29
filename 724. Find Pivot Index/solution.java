class Solution {
    public int pivotIndex(int[] nums) {
        var sum_arr = 0;
        var left = 0;
        for (int x : nums)
            sum_arr += x;
        for (int i = 0; i < nums.length; i++) {
            if (left == sum_arr - left - nums[i])
                return i;
            left += nums[i];
        }
        return -1;
    }
}