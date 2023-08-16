class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2: return 0

        max_profit, buy_day, sell_day = 0, 0, 1

        while sell_day < len(prices):
            curr_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, curr_profit)

            if prices[buy_day] >= prices[sell_day]:
                buy_day = sell_day

            sell_day += 1

        return max_profit

        # TC: O(n)
        # SC: O(1)