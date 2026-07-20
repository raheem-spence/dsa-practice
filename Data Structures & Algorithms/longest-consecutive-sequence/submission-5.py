class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given: array of integers nums
        # goal: return length of longest consecutive subsequence that can be formed
        # where a consecutive sequence is a sequence of elements in which each element is
        # 1 greater than the previous elements
        # pattern: ?
        # approach: ?

        # [2, 20, 4, 10, 3, 5]

        longest_seq = 0
        nums_set = set(nums)

        for num in nums_set:
            current_seq_length = 0
            if num - 1 not in nums_set:
                current_seq_length += 1

                while num + 1 in nums_set:
                    current_seq_length += 1
                    num += 1
            longest_seq = max(longest_seq, current_seq_length)

        return longest_seq

