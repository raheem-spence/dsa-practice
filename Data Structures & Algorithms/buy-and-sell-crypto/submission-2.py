class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                current_profit = prices[r] - prices[l]
                max_profit = max(max_profit, current_profit)
                r += 1
        return max_profit