class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given: an array nums, integer k
        # goal: return the k most frequent elements
        # approach: bucket sort

        my_dict = {}

        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)

        max_count = 0

        for num, count in my_dict.items():
            curr_count = count
            max_count = max(max_count, curr_count)

        
        buckets = [[] for i in range(max_count + 1)]

        for num, count in my_dict.items():
            buckets[count].append(num)

        most_freq = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq
