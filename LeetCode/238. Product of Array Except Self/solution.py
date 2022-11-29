class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
# Time = O(n)
# Space = O(1) = output array (answer) is not considered in this analysis

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
        
#         for i in range(len(nums)):
#             product = 1
#             for j in range(len(nums)):
#                 if j != i: product *= nums[j]
#             answer.append(product)
        
#         return answer
# time = O(n^2)
# space = O(n)
    
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#         product = 1
        
#         zeroCount = 0
#         for j in range(len(nums)):
#             if nums[j] != 0: 
#                 product *= nums[j]
#             else: 
#                 zeroCount += 1
        
#         if zeroCount > 1:
#             return [0] * len(nums)
        
#         if zeroCount == 1:
#             for i in range(len(nums)):
#                 if nums[i] == 0:
#                     answer.append(product)
#                 else:
#                     answer.append(0)
#             return answer
        
#         if zeroCount == 0:
#             for i in range(len(nums)):
#                 answer.append(product // nums[i]) # wrong we can't se the diivision
#             return answer
        
#         Time = O(n)
#         Space = O(n)
        
    
    
    
    