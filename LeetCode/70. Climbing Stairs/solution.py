class Solution:
    def climbStairs(self, n: int, memo = {1:1, 2:2}) -> int:
        if n not in memo.keys():
            memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        return memo[n]

#     Time = O(n)
#     Space = O(n) the memo

# Using DP - optimal solution
class Solution:
    def climbStairs(self, n: int, memo={1: 1, 2: 2}) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

#     Time = O(n)
#     Space = O(1)
