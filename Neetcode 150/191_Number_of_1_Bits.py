class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        
        while n != 0:
            ones += n % 2
            n = n >> 1
            
        return ones
        
        # TC: O(1) number of 1 bits max ~32
        # SC: O(1)