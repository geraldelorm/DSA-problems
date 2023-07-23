class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def numberOfWays(coinIndex, amountLeft):
            if (coinIndex, amountLeft) in memo:
                return memo[(coinIndex, amountLeft)]
            if amountLeft == 0:
                return 1 
            if coinIndex >= len(coins) or amountLeft < 0:
                return 0
            
            if coins[coinIndex] > amountLeft: #one way forward ~ try next coins
                memo[(coinIndex, amountLeft)] = numberOfWays(coinIndex + 1, amountLeft)
            else: #two posible ways
                memo[(coinIndex, amountLeft)] = numberOfWays(coinIndex + 1, amountLeft) + numberOfWays(coinIndex, amountLeft - coins[coinIndex])
                
            return memo[(coinIndex, amountLeft)] 
        
        return numberOfWays(0, amount)
        
#         TC: O(coins * amount)
#         SC: O(coins * amount)