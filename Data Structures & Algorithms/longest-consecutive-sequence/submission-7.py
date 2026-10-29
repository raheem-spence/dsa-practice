class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given: an array of integers nums
        # goal: return the length of the longest consecutive sequence
        # approach: use a hashset to store unique values from nums
        # start a sequence once you have found the smallest number in the set then extend the sequence only if the number exactly 1 greater than current number is in set

        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            length = 1

            while num + length in nums_set:
                length += 1
            
            longest = max(longest, length)
        
        return longest
