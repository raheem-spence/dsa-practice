class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict()
        count_t = dict()

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t






