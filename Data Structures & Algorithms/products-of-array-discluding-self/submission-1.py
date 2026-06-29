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

        for i in range(len(nums)):
            j = -i - 1
            left_mult[i] = left
            left *= nums[i]
            right_mult[j] = right
            right *= nums[j]

        
        
        return [l*r for l, r in zip(left_mult, right_mult)]


