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
        r = len(nums) - 1

        while l < r:
            if nums[l] == 0:
                zero = nums.pop(l)
                nums.append(zero)
                r -= 1
            else:
                l += 1
                continue