class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(len(res)):
            res[i] = self.numberOfBits(i)       
        return res
        
    def numberOfBits(self, n):
        res = 0
        while n:
            n, dig = divmod(n, 2)
            res += dig
            
        return res
    
    # TC: O(nlogn)
    # SC: O(1)