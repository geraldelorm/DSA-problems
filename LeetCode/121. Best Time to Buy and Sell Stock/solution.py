# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0
#         b, s = 0, len(prices) - 1

#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] > prices[i]:
#                     currProfit = prices[j] - prices[i]
#                     maxProfit = max(maxProfit, currProfit)

#         return maxProfit

#     Time = O(n^2)
#     Space = O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buyDay = 0, 0

        for sellDay in range(1, len(prices)):
            currProfit = prices[sellDay] - prices[buyDay]
            maxProfit = max(maxProfit, currProfit)

            if prices[sellDay] < prices[buyDay]:
                buyDay = sellDay

        return maxProfit

# Time = O(n)
# Space = O(1)
