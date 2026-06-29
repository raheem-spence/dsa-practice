class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach: Sort the array first. Then use three pointers i, j, k and
        # return a list of triplits
        
        # If the sum of all three numbers at each pointer is less than zero,
        # reset move the i and j pointer to the left one, otherwise move j and k
        # to the left

        nums.sort()

        triplets = []
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            # Two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum == 0:
                    triplets.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1

        return triplets

