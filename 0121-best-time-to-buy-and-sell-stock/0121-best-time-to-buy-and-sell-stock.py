class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # brute force approach
        # max_profit = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] <= prices[i]:
        #             continue
        #         else:
        #             profit = prices[j] - prices[i]
        #             max_profit = max(profit, max_profit)

        # return max_profit

        # optimal approach

        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])

        return max_profit


        