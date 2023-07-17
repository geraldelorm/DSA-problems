# # Brute Force
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
        
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 curr_max = sum(nums[i: j + 1])
#                 max_sum = max(max_sum, curr_max)
                
#         return max_sum

# Time O(n^3)
   
# Optimal - Greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_max = nums[0], 0
        
        for n in nums:
            if curr_max < 0:
                curr_max = 0
                
            curr_max += n
            max_sum = max(max_sum, curr_max)
            
            
        return max_sum
    
    
# Time O(n)