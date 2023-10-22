class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        look_up = set()
        for n in nums:
            look_up.add(n)    
            
        for i in range(len(nums) + 1):
            if i not in look_up:
                return i
            
        # TC: O(n)
        # SC: O(n)
        
        
# Reduce space with sum of both and - substract
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res

            
        # TC: O(n)
        # SC: O(1)
        
# Can you code the bit munipulation solution?