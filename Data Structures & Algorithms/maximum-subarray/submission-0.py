class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach: Keep track of the maximum subarray and current sum where
        # the maximum subarray starts out as the first element. Loop through
        # the array adding each subsequent element to the current sum. If
        # current sum is greater than maximum subarray then update it.

        # Note: if the current sum is less than 0, we set curent sum back to zero

        max_sub = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sub = max(max_sub, curr_sum)
        return max_sub