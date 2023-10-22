# Brute Force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = nums[0]
        for i in range(len(nums)):
            currMax = 1
            for j in range(i, len(nums)):
                currMax *= nums[j]
                res = (max(res, currMax))
        
        return res
    
#     TC: O(N^2)
#     SC: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = 1
        res = nums[0]
        
        for n in nums:
            temp = currMax * n
            currMax = max(n, temp, currMin * n)
            currMin = min(n, temp, currMin * n)
            
            res = max(res, currMax)
            
        return res
                      
#     TC: O(N)          
#     SC: O(1)