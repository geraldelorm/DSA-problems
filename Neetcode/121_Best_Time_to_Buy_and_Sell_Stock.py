class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            
            if prices[sell] <= prices[buy]:
                buy = sell
            
            sell += 1

        return max_profit
    
    # TC: O(n)
    # SC: O(1)