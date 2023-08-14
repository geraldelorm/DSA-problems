# Brute Force
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        def isValid(_str):
            distict = {}
            for c in _str:
               distict[c] = distict.get(c, 0) + 1
            return len(distict) <= 2

        for i in range(len(s)):
            for j in range(i, len(s)):
                if not isValid(s[i: j + 1]):
                    break
                max_len = max(max_len, len(s[i: j + 1]))

        return max_len

        # TC: O(n^3)
        # SC: O(n)

# Optimal ~ Two pinters 
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        left = right = 0

        distinct = {}

        while right < len(s):
            distinct[s[right]] = distinct.get(s[right], 0) + 1

            while len(distinct) > 2:
                distinct[s[left]] -= 1
                if  distinct[s[left]] == 0:
                    del distinct[s[left]]
                left += 1

            max_len = max(max_len, (right - left) + 1)
            right += 1

        return max_len
            
        # TC: O(n)
        # SC: O(n)
