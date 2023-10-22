class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        b, s = 0, len(prices) - 1

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    currProfit = prices[j] - prices[i]
                    maxProfit = max(maxProfit, currProfit)

        return maxProfit

# Time = O(n^2)
# Space = O(1)


#Optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay, sellDay = 0, 1

        while sellDay < len(prices):
            currProfit = prices[sellDay] - prices[buyDay]
            maxProfit = max(maxProfit, currProfit)
            if prices[buyDay] >= prices[sellDay]:
                buyDay = sellDay

            sellDay += 1

        return maxProfit

# TC: O(n)
# SC: O(1)