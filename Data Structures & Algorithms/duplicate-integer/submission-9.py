class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given: array of ints
        # return: True if duplicates else False
        # goal/approach: use hash set on nums arr and compare to original

        nums_set = set(nums)

        return len(nums_set) != len(nums)