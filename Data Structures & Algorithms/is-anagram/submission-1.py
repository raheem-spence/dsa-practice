class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the two strings have unequal lengths they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create dict for each to track character frequency
        count_s, count_t = {}, {}

        # Loop through the length of one string
        # and update the character counts for each string

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t


        