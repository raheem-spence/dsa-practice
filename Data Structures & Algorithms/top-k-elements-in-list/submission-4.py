class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store num:frequency pairs
        my_dict = {}

        # Loop through array and add num and its frequency
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        
        # Now loop through the dict for keys and values to create
        # a list of lists where each index represents a bucket for each
        # frequency

        # Tells us the max amount of buckets
        max_freq = 0
        
        for num, freq in my_dict.items():
            current_freq = freq
            max_freq = max(max_freq, current_freq)
        
        bucket_list = [[] for _ in range(max_freq + 1)]

        for num, freq in my_dict.items():
            bucket_list[freq].append(num)

        most_freq = []
        for freq in range(len(bucket_list)-1, 0, -1):
            for num in bucket_list[freq]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq

     

            


