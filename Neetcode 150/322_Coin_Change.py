#Brute Force
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_coins = float("inf")
        
        def dfs(number_of_coins, amount):
            if amount == 0:
                self.min_coins = min(self.min_coins, number_of_coins)
                return
            if amount < 0:
                return
            for coin in coins:
                dfs(number_of_coins + 1, amount - coin)
                
        dfs(0, amount)
        return self.min_coins if self.min_coins != float("inf") else -1
    
    # TC:O(amount ^ coins)
    # SC: O(amount)
    
    
#Memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(remender, memo = {}):
            if remender in memo:
                return memo[remender]
            if remender == 0:
                return 0
            if remender < 0:
                return -1
            
            min_coins = float("inf")
            for coin in coins:
                res = dfs(remender - coin, memo)
                if res != -1:
                    min_coins = min(1 + res, min_coins)
                    
            memo[remender] =  min_coins 
            return min_coins if min_coins != float("inf") else -1
                
        return dfs(amount)
    
    # TC:O(amount * coins)
    # SC: O(amount)
    
    
#Memoization - using functools lru_cache
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dfs(remender):
            if remender == 0:
                return 0
            if remender < 0:
                return -1
            
            min_coins = float("inf")
            for coin in coins:
                res = dfs(remender - coin)
                if res != -1:
                    min_coins = min(1 + res, min_coins)
                    
            return min_coins if min_coins != float("inf") else -1
                
        return dfs(amount)
    
    # TC:O(amount * coins)
    # SC: O(amount)
    
#Tabulation 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #create a dp table
        dp = [math.inf] * (amount + 1)
        dp[0] = 0 # for amount 0
        
        for curr_amount in range(1, len(dp)): #for each amount from 1 to amount      
            for coin in coins: #check for valid coins and add 1 to prev coins needed
                if curr_amount - coin >= 0: 
                    dp[curr_amount] = min(1+ dp[curr_amount - coin], dp[curr_amount])
        
        return dp[amount] if dp[amount] != math.inf else -1
    
    # TC:O(amount * coins)
    # SC: O(amount)