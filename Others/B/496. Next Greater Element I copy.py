# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         hash_map = {v:i for i, v in enumerate(nums1)}
#         res = [-1] * len(nums1)
            
#         for i, v in enumerate(nums2):
#             if v not in hash_map:
#                 continue
#             for j in range(i + 1, len(nums2)):
#                 if nums2[j] > v:
#                     idx = hash_map[v]
#                     res[idx] = nums2[j]
#                     break
#         return res
    
# # Space = O(n) where n = num1
# # Time O(n*m) wnere n = num1 and m = nums2

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         hash_map = {v:i for i, v in enumerate(nums2)}
#         res, found = [], False
            
#         for i, v in enumerate(nums1):
#             idx = hash_map[v]
#             for cv in nums2[idx:]:
#                 if cv > v:
#                     res.append(cv)
#                     found = True
#                     break
#             if not found:
#                 res.append(-1)
#             found = False
#         return res
    
# # Space = O(m) where n = num2
# # Time O(n*m) wnere n = num1 and m = nums2

# Optimal O(n + m) solution
class Solution:
     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIdx = {v:i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
            
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = numsIdx[val]
                res[idx] = curr
            if curr in numsIdx:
                stack.append(curr)
                
        return res
# Space = O(n) where n = num2
# Time O(n + m) wnere n = num1 and m = nums2