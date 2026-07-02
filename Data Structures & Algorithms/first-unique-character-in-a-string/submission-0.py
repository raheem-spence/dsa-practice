class Solution:
    def firstUniqChar(self, s: str) -> int:
        # given: a string s
        # goal: find the first non-repeating character in it
        # and return its index. If it doesnt exist, return -1
        # pattern: arrays and hashing
        # approach: use a hash map to store frequency character counts where
        # keys are counts and values are indices
        # then loop through hash map to find character with frequency of 1
        # and return that index. if none with count of 1 return -1

        char_count = {}

        for char in s:
            count = 1 + char_count.get(char, 0)
            char_count[char] = count

        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1

