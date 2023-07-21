#Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]  
        
        def rob(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]     
            if len(nums) == 2:
                return max(nums)
            
            return max((nums[0] + rob(nums[2:])), rob(nums[1:]))
        
        return max(rob(nums[0:-1]), rob(nums[1:]))
    
# TC: O(2^n)
# SC: O(n)


#DP with Memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]  
        
        return max(self.robfrom(nums[0:-1], 0, {}), self.robfrom(nums[1:], 0, {}))
        
    def robfrom(self, nums, i, memo):
        if i >= len(nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = max((nums[i] + self.robfrom(nums, i + 2, memo)), self.robfrom(nums, i + 1, memo))

        return memo[i]
        
    
# TC: O(n)
# SC: O(n)


# DP with smart tabulization
class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1: return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        prev_rob = curr_rob = 0
        
        for n in nums:
            newOptimalRob = max(curr_rob, prev_rob + n)
            prev_rob = curr_rob
            curr_rob = newOptimalRob

        return curr_rob
        
    
# TC: O(n)
# SC: O(1)