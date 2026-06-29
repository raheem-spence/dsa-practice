class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given: two strings
        # return: true if strs are anagrams else false
        # goal: keep track of characters for each string then compare

        # approach: hash map character frequency count
        # check if lengths are equal else return false immediately!

        # example:
        #  s = "jam", t = "jar"

        if len(s) != len(t):
            return False

        dict_counts = {}

        for char in s:
            count = 1 + dict_counts.get(char, 0)
            dict_counts[char] = count
        
        for char in t:
            count = dict_counts.get(char, 0)
            
            if count == 0:
                return False
            count -= 1
            dict_counts[char] = count

        return True
            
        