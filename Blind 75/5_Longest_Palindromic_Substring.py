#Brute Force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrom = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrom(s[i:j + 1]):
                    if len(max_palindrom) < j + 1 - i:
                        max_palindrom = s[i:j + 1]
                    
        return max_palindrom
    
    def isPalindrom(self, sub):
        return sub == sub[::-1]
    
#     TC: O(n^3)
#     SC: (O(n^2))


# Optimal:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.resLen = 0
        
        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.resLen:
                    self.res = s[l : r + 1]
                    self.resLen = r - l + 1
                l -= 1
                r += 1
                

        for i in range(len(s)):
            # odd length
            l, r = i, i
            check(l, r)

            # even length
            l, r = i, i + 1
            check(l, r)

        return self.res
    
#     TC: O(n^2)
#     SC: (O(1))