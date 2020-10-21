class Solution {
    public int removeDuplicates(int[] nums) 
    {
        int len = nums.length;
        var index = 0;
        for(int i = 0; i< len ; i++){
            if(nums[index]!=nums[i]){
                index++;
                nums[index] = nums[i];
            }
        }
       
                return index+1;
    }
}
