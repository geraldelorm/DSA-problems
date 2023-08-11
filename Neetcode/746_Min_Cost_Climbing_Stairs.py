# Brute Force
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(i):
            if i >= len(cost):
                return 0
            
            return min(cost[i] + climb(i + 1), cost[i] + climb(i + 2))
        
        return min(climb(0), climb(1))
                
#         TC: O(2^n)
#         SC: O(n)

# Memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(i, memo):
            if i in memo:
                return memo[i]
            if i > len(cost):
                return 0
            
            memo[i] = min(cost[i] + climb(i + 1, memo), cost[i] + climb(i + 2, memo))
            return memo[i]
        
        memo = {len(cost): 0}
        return min(climb(0, memo), climb(1, memo))
                
#         TC: O(n)
#         SC: O(n)