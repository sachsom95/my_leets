class Solution {
    public int[] shuffle(int[] nums, int n) {
        var ps = 0;
        var pf = n;
        int [] arr = new int[nums.length];
        var index = 0;
        for(int i = 0 ; i<n;i++){
            
            arr[index++] = nums[ps];
            arr[index] = nums[pf];
            ps++;
            pf++;
            index++;
            
        }
        return arr;
        
    }
}
