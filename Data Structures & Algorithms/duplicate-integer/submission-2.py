class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_nums = set(nums)

        if len(unique_nums) == len(nums):
            return False
        else:
            return True