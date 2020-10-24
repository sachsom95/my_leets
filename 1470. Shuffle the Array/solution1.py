class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pf = n
        ps = 0
        lst = []
        for x in range(n):
            lst.append(nums[ps])
            lst.append(nums[pf])
            ps+=1
            pf+=1
        
        return(lst)
