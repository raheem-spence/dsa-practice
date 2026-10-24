class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given: an integer array nums, an integer k
        # goal: return the top k most frequent elements
        # approach: bucket sort

        # hashmap num -> count
        count_map = {}
        max_count = 0
       
        # fill hashmap
        for num in nums:
            count = count_map.get(num, 0) + 1
            count_map[num] = count
        
        for num, count in count_map.items():
            max_count = max(max_count, count)

        # buckets where each index corresponds to the count of a number
        buckets = [[] for i in range(max_count + 1)]

        # fill buckets
        for num, count in count_map.items():
            buckets[count].append(num)
        
        most_freq = []

        # loop backwards over buckets to return the top k most frequent elements
        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                most_freq.append(num)

                if len(most_freq) == k:
                    return most_freq
