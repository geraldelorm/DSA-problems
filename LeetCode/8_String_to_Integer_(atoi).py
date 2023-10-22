class Solution:
    def myAtoi(self, s: str) -> int:
        str = s.strip()
        if not str: return 0
        
        sign = -1 if str[0] == '-' else 1
        str = str[1:] if str[0] in ["-", "+"] else str
            
        res = 0
        
        for c in str:
            if not c.isdigit():
                break
            res = (res * 10) + int(c)
            
            if res * sign >= 2**31 - 1:
                return 2**31 - 1
            if res * sign <= -2**31:
                return -2**31
            
        return res * sign
    
# Time = O(n)
# Space = O(1)