#Using Hashset - lookup
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
            
        return False
# Time = O(n)
# Space = O(n)


#Using inplace sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()        
        for i in range(len(nums) - 1 ):
            if nums[i] == nums[i + 1]:
                return True
            
        return False
# Time = O(nlogn)
# Space = O(1)