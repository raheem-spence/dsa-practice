class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given: integer array nums 
        # goal: return an array `output` where `output[i]` is the product of
        # all elements of `nums` except `nums[i]`
        # pattern: prefix / suffix product
        # approach: make a left to right pass to store the product of all elements
        # to left of each index and store it in `output`
        # make a right to left pass to maintain a running right product then   
        # multiply each stored left product by the current right product to obtain
        # the final output

        output = []
        product = 1

        # first pass to store the product of all elements to the left of current index
        for i in range(len(nums)):
            output.append(product)
            product *= nums[i]

        # second pass to multiply running right product by stored left product
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output

