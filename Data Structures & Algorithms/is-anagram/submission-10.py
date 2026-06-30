class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given: two strs 
        # return: True if anagrams else False
        # goal/approach: immediately return False if lens are unequal
        # use character frequency hash map to keep track
        # of char count s str then decrement count from hash map 
        # if t str matches, if no match return False

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
        