class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given: a string s
        # goal: return True if palindrom, else False
        # pattern: two pointers
        # approach: left pointer starts at beginning, right pointer starts
        # at the end, compare characters at each pointer
        # if characters are different then return False
        # time: O(n), one pass through string
        # space: O(1), constant space for pointers

        # example: "No lemon, no melon"

        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -=1 
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
