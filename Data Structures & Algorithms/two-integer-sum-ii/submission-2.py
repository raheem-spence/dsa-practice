class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given: array of integers numbers sorted in non-decreasing order
        # goal: return the indices (1-indexed) of two numbers that add up to target and follow the given conditions
        # pattern: two pointers 
        # approach: we can start with each pointer at opposite ends. we check if the two numbers at each pointer adds to target, return the indices (1-indexed) if so, else if the sum is less than target we move the left pointer inwards, and vice versa if the sum if greater than target. we move the pointers this way because the array is sorted so say the sum of two numbers is less than target, the only way to reach target is to move the left pointer inward to a larger number and vice versa 
        # time: O(n), one pass through array
        # space: O(1), only using pointers 

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        
