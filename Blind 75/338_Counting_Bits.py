class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            count = 0
            while n > 0:
                count += n % 2
                n >>= 1
            return count
                
        res = []
        for i in range(n + 1):
            res.append(countOnes(i))
            
        return res
    
#     TC: O(NlogN)
#     SC: O(N)
# 
# Optimal SOlution
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp_table = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            #check if offset need to be updated once we reach a signinficant bit
            if offset * 2 == i:
                offset = i
                
            dp_table[i] = 1 + dp_table[i - offset]
            
        return dp_table
    
#     TC: O(N)
#     SC: O(N)