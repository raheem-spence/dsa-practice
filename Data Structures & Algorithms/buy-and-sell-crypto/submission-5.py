class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given: array of integers -- prices where each index is the price
        # of a NeetCoin on that day
        # goal: return max profit
        # pattern: sliding window
        # approach: use two pointers, one left one right, we want to lowest
        # price for the left and highest for the right pointer. Once we find
        # the lowest price for the left, we extend the right pointer and slide 
        # the window to find the highest price. If a new lower price is found,
        # we move out left pointer

        l = 0
        r = l + 1

        res = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l += 1
                r = l + 1
                continue
            profit = prices[r] - prices[l]

            res = max(res, profit)
            r += 1
        
        return res
