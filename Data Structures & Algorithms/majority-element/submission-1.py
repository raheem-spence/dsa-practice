class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # given: array nums of size n
        # goal: return majority element -- one that appears more than n / 2 times
        # pattern: arrays and hashing
        # approach: use hash map for frequency count of numbers
        # return the number that is above threshold 

        nums_count = {}
        threshold = len(nums) / 2
        majority_element = 0

        for num in nums:
            count = 1 + nums_count.get(num, 0)
            nums_count[num] = count
        
        for num, count in nums_count.items():
            if count > threshold:
                return num
    
