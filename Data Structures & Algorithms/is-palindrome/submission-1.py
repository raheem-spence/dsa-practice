class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach: use two pointers, one at each end of the string
        # to compare character pairs, if character pairs are not equal,
        # then the string is not a palindrome and we can return False
        # Otherwise, we keep moving the pointers towards each other. 
        # If they cross or are equal to each other we know we have a
        # palindrome

        # Note: We need convert uppercase to lowercase becuase a palindrome 
        # is case-insensitive and we need to ignore anything that is not
        # alphanumeric (i.e. spaces, punctuation marks, etc.)

        # Create two pointers at each end
        l = 0
        r = len(s) - 1

        # Loop until the two pointers have met or pass one another
        while l < r:
            # Skip over non-alphanumeric characters
            if not s[l].isalnum():
                l += 1
                continue
            
            if not s[r].isalnum():
                r -= 1
                continue

            # Compare lowercase alphanumeric characters
            if s[l].lower() != s[r].lower():
                return False

            # Move pointers inward
            l += 1
            r -= 1
        
        # Valid palindrome if l and r meet or pass one another
        return True


        # Time: O(n) visit each character at most once
        # Space: O(1), no extra data structures