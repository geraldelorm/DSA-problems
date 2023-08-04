#Sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False
    # TC: O(NlogN)
    # SC: O(1)


#HashSet
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
            
        return False
    # TC: O(n)
    # SC: O(n)