class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # given: integer array `nums` and an integer `k`
        # goal: return true if there are two distinct indices `i` and `j` in the array such that
        # `nums[i] == nums[j]` and `abs(i - j) <= k, otherwise false
        # pattern: arrays and hashing
        # approach: use a hash map to see store 


        num_map = {}

        for i, num in enumerate(nums):
            if num in num_map and abs(i - num_map[num]) <= k:
                return True
            num_map[num] = i
        
        return False



        