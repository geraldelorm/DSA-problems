# Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max((nums[0] + nums[2]), nums[1])
        
        return max((nums[0] + self.rob(nums[2:])), self.rob(nums[1:]))
    
    #TC: O(2^n)
    #SC: O(n)
        
        
# Optimal DP with memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        
        return self.robFrom(nums, 0)
        
    def robFrom(self, nums, i):
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        self.memo[i] = max((nums[i] + self.robFrom(nums, i + 2)), self.robFrom(nums, i + 1))
        
        return self.memo[i]
    
    #TC: O(n)
    #SC: O(n)
    
    
# Optimal DP with optimized tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob, curr_rob = 0, 0
        
        for n in nums:
            optimal_rob = max(curr_rob, prev_rob + n)
            prev_rob = curr_rob
            curr_rob = optimal_rob
            
        return curr_rob
    
    #TC: O(n)
    #SC: O(1)