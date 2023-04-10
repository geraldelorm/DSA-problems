class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        
        isNeg = x < 0
        res = ""
        
        x = abs(x)
        
        while x > 0:
            res += str(x % 10)
            x = x // 10

        
        if isNeg: 
            res = int(res) * -1 
        else:
            res = int(res)
        
        if -2**31 > res or res > 2**31: return 0
        
        return res
        
        
# Time = O(logN) - number of digits in N
# Space = O(1)
        