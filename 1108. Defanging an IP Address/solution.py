class Solution:
    def defangIPaddr(self, address: str) -> str:
        data = ""
        for x in address:
            if x =='.':
                data+='[.]'
            else:
                data+=x
        return(data)
                