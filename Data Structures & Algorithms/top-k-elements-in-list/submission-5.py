class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary of num (key) and count/frequency (value)
        count_dict = {}

        # Add each num:count pair to dictionary
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        # Keep track of max count which determines the size of 
        # our list of buckets
        max_count = 0

        for num, count in count_dict.items():
            current_count = count
            max_count = max(max_count, current_count)


        # List of lists to store the nums at indices corresponding to their
        # count (e.g. [2] at index 1 means the num 2 appears once in array)
        # We use the max_count to determine the length of of buckets list

        # NOTE! We have to add 1 because lists are zero-based, so adding one
        # lines the indices up with count(or frequency)
        buckets = [[] for i in range(max_count + 1)]

        # Now we append the num to the correct bucket based on its count.
        # The whole point of finding the max_count is to map the count to an
        # index position. The same for creating out list of lists.
        # Note, the at the zeroith position, there will always be an empty unused
        # list.

        for num, count in count_dict.items():
            buckets[count].append(num)

        # Last but not least, we loop through the buckets list and grab the top
        # k frequent elements
        # For this we need a nested loop, the outer loop does no work, it just
        # tells us which bucket to loop at.
        # Note, we want to start at the end of the list and iterate to the
        # beginning so its easy to grap top k elements
        # The inner loop does all the work

        most_freq = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq







