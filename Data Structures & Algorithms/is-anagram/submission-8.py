class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given: two strings
        # return: true if strs are anagrams else false
        # goal: keep track of characters for each string then compare

        # approach: hash map to keep track of the count of each char
        # check if lengths are equal else return false immediately!

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for char in s:
            count_s = 1 + dict_s.get(char, 0)
            dict_s[char] = count_s
        
        for char in t:
            count_t = 1 + dict_t.get(char, 0)
            dict_t[char] = count_t

        return dict_s == dict_t
            
        