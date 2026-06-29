class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach: we need an array containing left multipliers and an array
        # containing right multipliers where if we take multiply the multipliers
        # at corresponding positions, we will get the product of the array
        # except self at that index

        left = 1
        right = 1

        left_mult = [0] * len(nums)
        right_mult = [0] * len(nums)

        res = []

        # Left multiplier list
        for i in range(len(nums)):
            left_mult[i] = left
            left = left * nums[i]

        # Right multiplier list
        for i in range(len(nums) - 1, -1, -1):
            right_mult[i] = right
            right = right * nums[i]

        # Resultiing list
        for i in range(len(nums)):
            res.append(left_mult[i] * right_mult[i])
        
        return res


