#Using a hashmap to look-up differences
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            hashmap[v] = i
            
# Time - O(n)
# Space - O(n)