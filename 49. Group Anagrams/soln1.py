class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_table = {}
        for word in strs:
            data = ''.join(sorted(word))
            if(data not in hash_table):
                hash_table[data] = [word]
            else:
                hash_table[data].append(word)

        return hash_table.values()
