#Brute Force
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        return self.climbStairs(n -1) + self.climbStairs(n - 2)
    
    # TC: O(2^n)
    # SC: (n)
    
# Memoization
class Solution:
    def climbStairs(self, n: int, memo = {0: 1}) -> int:
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n -1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]
    
    # TC: O(n)
    # SC: O(n)
    
    
#Tabulation
class Solution:
    def climbStairs(self, n: int, memo = {0: 1}) -> int:
        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1
        
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]   
        
        return table[n]
    
    # TC: O(n)
    # SC: O(n)