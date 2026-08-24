class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # given: integer array nums
        # goal: return all triplets where nums[i] + nums[j] + nums[k] == 0
        # pattern: two pointers + sorting
        # approach: O(n^2)
        # space: O()

        # -nums[i] == nums[j] + nums[k]
        # [-4, 0, -1, -1, 1, 2]
        # [1, 2, 3, 4, 5, 6]

        nums.sort()

        res = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 

                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return res

