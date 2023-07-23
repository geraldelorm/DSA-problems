class Solution:
    def numDecodings(self, s: str) -> int:
        lookup = {len(s) : 1}
        
        def waysToDecodeStratingWith(i):
            if i in lookup:
                return lookup[i]
            if s[i] == '0':
                return 0
            
            ways = waysToDecodeStratingWith(i + 1);
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                ways += waysToDecodeStratingWith(i + 2)
            
            lookup[i] = ways
            return ways
            
        return waysToDecodeStratingWith(0)
    
# TC: O(N)
# SC: O(N)