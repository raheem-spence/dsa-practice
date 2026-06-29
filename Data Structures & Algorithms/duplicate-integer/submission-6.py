class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Turn the array into a set and compare lenth of array to set

        nums_set = set(nums);
        return len(nums) != len(nums_set)
        