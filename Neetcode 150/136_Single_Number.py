# Using Map
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = defaultdict(int)
        
        for n in nums:
            table[n] += 1
            
        for k in table:
            if table[k] == 1:
                return k
            
    # TC: O(N)
    # SC: O(N)