# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# E.g
# [5, 3, 10] = 7
# [5, 4, 3]  = 0
# [7,1,5,3,6,4] = 5
# [7,6,4,3,1] = 0

# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)

        return max_profit

# Time = O(N^2)
# Space = O(1)

# Optimal Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell

            curr_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, curr_profit)

        return max_profit
# Time = O(N)
# Space = O(1)
