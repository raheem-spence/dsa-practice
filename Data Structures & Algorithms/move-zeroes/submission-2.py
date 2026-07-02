class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # given: array nums
        # goal: move all 0's to the end of array while maintaining relative
        # order of non-zero elements
        # pattern: 
        # approach: use two pointers??

        l = 0
        r = 0

        while r < len(nums):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1