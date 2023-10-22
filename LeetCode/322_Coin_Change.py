class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        if amount == 0 or n == 0:
            return 0

        dp = [[0] * (amount + 1) for i in range(n + 1)]

        for i in range(1, amount + 1):
            dp[0][i] = float('inf')

        for i in range(1, len(dp)):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        
#     n = coins; m = amount
#     Time = O(nm)
#     Space = O(nm)
