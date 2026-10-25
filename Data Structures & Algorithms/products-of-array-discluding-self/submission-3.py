class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given: an integer array nums
        # goal: return an array 'output' where 'output[i]' is the product of all the elements of nums except 'nums[i]'
        # approach: 

        output = []

        left_product = 1
        
        for i in range(len(nums)):
            output.append(left_product)
            left_product *= nums[i]
        
        right_product = 1
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
