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
        maxProfit = 0
        left, right = 0, 1  # buy sell

        while right < len(prices):
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currProfit)
            else:
                left = right
            right += 1

        return maxProfit

# Time = O(n)
# Space = O(1)
