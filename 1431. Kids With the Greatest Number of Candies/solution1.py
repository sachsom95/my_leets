class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        for x in candies:
            if x > max:
                max = x
        lst=[]
        for x in candies:
            if (x+extraCandies) >= max:
                lst.append(True)
            else:
                lst.append(False)
        
        return lst
