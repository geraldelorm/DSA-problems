#Brute Force - check all posible steps that can lead to top(n == 0)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
#Time = O(2^n)
#SC: O(n)


#DP = memo
class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo) 
        return memo[n]
        
#Time = O(n)
#SC: O(n)


#DP = tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1] * (n + 1)
        
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        
        return table[n]
        
#Time = O(n)
#SC: O(n)



# Optimazied Space for tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

# TC: O(n)
# SC: O(1)