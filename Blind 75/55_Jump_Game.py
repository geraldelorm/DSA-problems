#DP 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def canJumpFromPos(nums, pos, memo):
            if pos in memo:
                return memo[pos]
            
            if pos == len(nums) - 1:
                memo[pos] = True
                return True
            
            furthestJump = min(pos + nums[pos], len(nums) - 1)
            
            for i in range(pos + 1, furthestJump + 1):
                if canJumpFromPos(nums, i, memo):
                    memo[pos] = True
                    return True
                
            memo[pos] = False
            return False
        
        return canJumpFromPos(nums, 0, {})
# Time = O(n^2)
# Space = O(n) recursion and memo
        
    
#Greedy 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i  
            
        return goal == 0 
        
# Time = O(n)

