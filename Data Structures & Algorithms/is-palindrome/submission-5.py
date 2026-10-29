class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given: a string s
        # goal: return true if it is a palindrome else false
        # pattern: two pointers
        # approach: start with two pointers on each end and check if they are pointing at the same character.


        l = 0
        r = len(s) - 1

        while l < r:
            # skip non-alphanumeric characters
            while l < len(s) and not s[l].isalnum():
                l += 1
                continue
            while r > l and not s[r].isalnum():
                r -= 1
                continue

            if l >= r:
                break
            if s[l].upper() != s[r].upper():
                return False
            else: 
                l += 1
                r -= 1
        return True
        