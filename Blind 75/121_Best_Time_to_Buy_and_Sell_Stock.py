class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        best = 0
        
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            best = max(best, profit)
            
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
            
        return best
    
#  Time = O(n)
# Space = O(1)