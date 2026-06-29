class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
                r += 1
                continue
            
            min_price = min(min_price, prices[l])
            current_profit = prices[r] - min_price
            max_profit = max(max_profit, current_profit)

            l += 1
            r += 1

        return max_profit