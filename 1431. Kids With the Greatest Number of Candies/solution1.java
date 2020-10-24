class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> arr = new ArrayList<>();
        var max = 0;
        for (int i:candies){
            if(i > max) max = i;
        }
        
        for (int i=0 ; i <candies.length;i++){
            if(candies[i]+extraCandies >= max) 
            {
                arr.add(true);
            }else
            {
                arr.add(false);
            }
        }
        return arr;
    }
}
