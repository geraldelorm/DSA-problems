#Using map
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSqrDigits(n):
            res = 0
            while n > 0:
                n, dig = divmod(n, 10)
                res += dig ** 2    
            return res 
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumSqrDigits(n)

        return n == 1
    
    # TC: O(logN)
    # SC: O(logn)
    
    
#Fast and Slow pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = self.sumSqrDigits(n), n
        
        while fast != slow:
            fast = self.sumSqrDigits(fast)
            fast = self.sumSqrDigits(fast)
            slow = self.sumSqrDigits(slow)
            
        return fast == 1
        
    def sumSqrDigits(self, n):
        res = 0
        while n > 0:
            n, dig = divmod(n, 10)
            res += dig ** 2    
        return res
    
    