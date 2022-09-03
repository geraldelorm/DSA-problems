class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i, b in enumerate(prices):
            for j, s in enumerate(prices):
                if j > i:
                    max_profit = max(max_profit, s - b)
        
        return max_profit
    
#     Time = O(n ^ 2)
#     Space = (1)

