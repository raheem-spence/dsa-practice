class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # given: array nums containing n integers from 0 to n
        # goal: return the single number in the range that is missing from nums
        # pattern:
        # approach: put nums in a set, loop through from 0 to n, return number
        # that is not in set
        
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = 0

        for num in nums:
            actual_sum += num
        
        return expected_sum - actual_sum
           