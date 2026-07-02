class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given: sorted array distinct numbers and a target integer
        # goal: return index of target if it exists, else return -1
        # pattern: binary search
        # approach: three pointers, one at beginning, one in middle, one at end
        # check for target at middle pointer, if found return index
        # otherwise, if number at middle is less than target, ignore left half
        # and repeat search. 
        # if number in middle is greater than target, ignore right half
        # repeat search
        # time: O(log n)
        # space: O(1)

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
              
            else:
                l = m + 1
        return -1