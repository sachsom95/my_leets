class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        pf, pl = 0, length-1
        while(pf < pl):
            while(not s[pf].isalnum() and (pf < pl)):
                pf += 1

            while(not s[pl].isalnum() and (pf < pl)):
                pl -= 1

            if(s[pf].lower() != s[pl].lower()):
                return False
            else:
                pf += 1
                pl -= 1
        else:
            return True
