class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        

        for num in nums:
            if num - 1 in nums_set:
                continue
            i = 1
            seq = 1
            while num + i in nums_set:
                nums_set.remove(num + i)
                seq += 1
                i += 1
            longest = max(longest, seq)

        return longest

        # Time: O(n), one pass through array
        # Space: O(n) for the set