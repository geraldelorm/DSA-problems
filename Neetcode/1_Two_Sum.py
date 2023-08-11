class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in look_up:
                return [look_up[diff], i]
            look_up[v] = i
            
        return []
    
    # TC: O(n)
    # SC: O(n)