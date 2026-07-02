class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given: array of integers -- prices where each index is the price
        # of a NeetCoin on that day
        # goal: return max profit
        # pattern: sliding window
        # approach: use two pointers
        # left tracks the best buy day so far
        # right scans each possible sell day
        # if prices[right] < prices[left] move left to right
        # calculate profit and update max
        # time: O(n)
        # space: O(1)

        l = 0
        r = l + 1

        res = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]

            res = max(res, profit)
            r += 1
        
        return res
