class Solution:
    def firstUniqChar(self, s: str) -> int:
        # given: a string s
        # goal: return index of first non-repeating character if exist, else -1
        # pattern: 
        # approach: use a hash map to store index and character count
        # loop through s and return the index of first character that has a count
        # of 1

        char_to_count = {}

        for char in s:
            count = 1 + char_to_count.get(char, 0)
            char_to_count[char] = count
        
        for i, char in enumerate(s):
            if char_to_count[char] == 1:
                return i
        return -1
