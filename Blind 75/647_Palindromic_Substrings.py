#Brute Force
class Solution:
    def countSubstrings(self, s: str) -> int:
        def palCheck(i, j):
            return s[i:j + 1] == s[i:j + 1][::-1]
        
        pals = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if palCheck(i, j):
                    pals += 1
        
        return pals
    
#     TC: O(n^3)
#     SC: O(n^2)
        
# Optimal
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countPals(l, r):
            pals = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                pals += 1
            return pals
                
        res = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            res += countPals(l, r)

            # even length
            l, r = i, i + 1
            res += countPals(l, r)

        return res
    
#     TC: O(n^2)
#     SC: O(1)