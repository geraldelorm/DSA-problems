# /**
# * @ param {number} amount
# * @ param {number[]} coins
# * @ return {number}
# */
# var change = function(amount, coins, memo={}) {
#     let key = amount + " ~ " + coins
#     if (key in memo) return memo[key]
#     if (amount == 0) return 1
#     let ways = 0
#     let currentCoin = coins[coins.length - 1]
#     for(let qty=0
#         qty * currentCoin <= amount
#         qty++) {
#         ways += change(amount - qty * currentCoin, coins.slice(0, -1), memo)
#     }
#     memo[key] = ways
#     return memo[key]
# }


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for j in range(amount+1)] for i in range(len(coins))]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = 1

                elif coins[i] > j:
                    dp[i][j] = dp[i - 1][j]

                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]

        return dp[len(coins) - 1][amount]


#     n = coins; m = amount
#     Time = O(nm)
#     Space = O(nm)
