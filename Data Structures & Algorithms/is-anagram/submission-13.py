class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # frequency count for one string
        dict_counts = {}

        for char in s:
            count = dict_counts.get(char, 0) + 1
            dict_counts[char] = count

        for char in t:
            count = dict_counts.get(char, 0)

            if count == 0:
                return False
        
            count -= 1
            dict_counts[char] = count
        
        return True