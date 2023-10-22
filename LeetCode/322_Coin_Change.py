class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != math.inf else -1
    
#     TC: O(coins * amount)
#     SC: O(amount)