class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # Approach:
            # Create a dictionary to keep track of values we've seen

            # Loop through array and check if complement of current num is
            # in the dict
            # Use enumerate to get index + value of each num in array

            # Note: we care about the indices so we must store them as values
            # so we can access them with .get() dict method

        # Time: O(n), must visit each number once in array
        # Space: O(n), n keys in the dictionary corresponding to n elements
        # in array

        nums_dict = {}

        for i, current_num in enumerate(nums):
            complement = target - current_num

            if complement in nums_dict:
                return [nums_dict.get(complement), i]
            else:
                nums_dict[current_num] = i