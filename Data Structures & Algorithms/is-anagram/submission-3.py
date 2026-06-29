class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach: Use a hash map to store characters as keys and their 
        # count as values for each string. Then compare the two hash maps.

        # Why? Anagrams of eachother have the same characters and the same
        # amount of each

        dict_s = {}
        dict_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
        return dict_t == dict_s