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
    
#     TC: O(n)
#     SC: O(N)