# Brute Force - Doesn't work results in duplicates 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        
        return res
    
        # TC:O(n^3)
        # SC: O(n)
        
        
# Optimal with sorting but 
class Solution:
    def __init__(self):
        self.res = []
        
    def twoSum(self, firstPick, nums): #O(n)
        left , right = firstPick + 1, len(nums) - 1
        
        while left < right:
            threeSum = nums[firstPick]  + nums[left] + nums[right]
            
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else: #threeSum found
                self.res.append([nums[firstPick], nums[left], nums[right]])
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        firstPick = 0
        for firstPick in range(len(nums)):
            if firstPick > 0 and nums[firstPick] == nums[firstPick - 1]:
                continue
                
            self.twoSum(firstPick, nums)  
            firstPick += 1
    
        return self.res
        # TC:O(n^2)
        # SC: O(n)