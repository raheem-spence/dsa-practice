class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # given: array nums containing n integers from 0 to n
        # goal: return the single number in the range that is missing from nums
        # pattern:
        # approach: put nums in a set, loop through from 0 to n, return number
        # that is not in set

        nums_set = set(nums)

        for num in range(0, len(nums)+ 1):
            if num not in nums_set:
                return num