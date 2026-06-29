class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given: array of ints
        # return: boolean if any value appears more than once
        # goal: check if array has any duplicates
        # approach: put arr into a set since sets do not contain duplicates


        nums_set = set(nums)

        return len(nums_set) != len(nums)