class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        

        for num in nums:
            # Check if start of sequence
            if num - 1 not in nums_set:
                seq_length = 0
                while num + seq_length in nums_set:
                    seq_length += 1
                longest = max(longest, seq_length)

        return longest

        # Time: O(n), one pass through array
        # Space: O(n) for the set