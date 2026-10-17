class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        # frequency map for s
        for char in s:
            count = dict_s.get(char, 0) + 1
            dict_s[char] = count

        for char in t:
            count = dict_t.get(char, 0) + 1
            dict_t[char] = count
        
        return dict_t == dict_s
