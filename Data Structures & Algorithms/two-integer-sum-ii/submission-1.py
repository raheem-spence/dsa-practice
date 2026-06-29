class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Approach: Two pointers at each end. Depending on if the
        # values at each pointer are greater than or equal to the target, 
        # we move one pointer.
        
        # Since the array is sorted in non-decreasing order, 
        # we know the largest element is at the end and smallest at the beginning.
        
        # For example, if the sum of the smallest and largest element 
        # is greater than target, we move the right pointer (end pointer)
        # to the left since to meet the target we need a smaller pair

        # On the other hand, if the sum of the smallest and largest element is
        # less than the target, we move the left pointer (start pointer) to the 
        # right.

        # This pattern applies to any two numbers we are adding up to meet target.

        # Once we find the two numbers, we return their indices (1-indexed)

        # We can use a while loop, while the left pointer is less than the right,
        # we keep traversing the array

        # Then we use conditionals to see if two numbers meet target

        # Shortened approach:
        # Two pointers on sorted array
        # Move left/right pointers based on sum to find target
        # Return 1-indexed result



        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        # Time: O(n) each number is visited at most once
        # Space: O(1), no extra data structures needed
