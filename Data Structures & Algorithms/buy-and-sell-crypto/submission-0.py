class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            l = i
            r = i + 1

            if r < len(prices) and prices[l] > prices[r]:
                continue
            
            while r < len(prices) and prices[r] > prices[l]:
                current_profit = prices[r] - prices[l]
                max_profit = max(max_profit, current_profit)

                r += 1

        return max_profit