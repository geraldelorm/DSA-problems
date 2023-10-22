class Solution:
    def fib(self, n: int) -> int:
        # return self.fib_bad(n)
        # return self.fib_memo(n)
        return self.fib_buttom_up(n)
             
        
    def fib_bad(self, n): #O(2^n)
        if n == 1 or n == 2:
            return 1
        return self.fib_bad(n - 2) + self.fib_bad(n - 1)
        
        
#     DP - memoization uses a recursive call stack
    def fib_memo(self, n, memo = {}): #O(n)
        if n in memo:
            return memo[n]
        
        if n == 1 or n == 2:
            return 1
        else:
            memo[n] = self.fib_memo(n -2, memo) + self.fib_memo(n -1, memo)
            
        return memo[n]
      
#     DP - buttom_up
    def fib_buttom_up(self, n): #O(n)
        if n == 0: return 0
        if n == 1 or n == 2:
            return 1
        
        b_up_arr = [None] * (n+1)
        b_up_arr[1] = 1
        b_up_arr[2] = 1
        
        for i in range(3, n + 1):
            b_up_arr[i] = b_up_arr[i - 1] + b_up_arr[i - 2]
            
        return b_up_arr[n]