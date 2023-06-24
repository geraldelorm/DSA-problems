class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i - 1]:
                continue
            else:
                self.twoSum(i, nums, res)
                        
        return res
    
    def twoSum(self, i, nums, res):
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]

            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([nums[i] , nums[l], nums[r]])
                r -= 1
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                    
                    
# Time O(N^2)
# Space O(N)