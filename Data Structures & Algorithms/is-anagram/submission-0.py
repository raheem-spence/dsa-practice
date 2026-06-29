class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s_dict = dict()
        t_dict = dict()

        # Count frequency of characters in string s
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        # Count frequency of characters in string t
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        # Compare dictionarys
        return s_dict == t_dict
        