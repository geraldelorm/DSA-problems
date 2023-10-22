class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, v in enumerate(nums):
            if v in seen and abs(seen[v] - i) <= k:
                return True
            seen[v] = i
            
        return False
    
#     TC: O(n)
#     SC: O(n)