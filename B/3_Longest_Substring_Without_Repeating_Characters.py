#Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            max_len = max(max_len, len(seen))
        return max_len

        # TC: O(N^2)
        # SC: O(N)


# Optimal ~ Two pointers
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = end = 0

        seen = set()
        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            
            seen.add(s[end])
            max_len = max(max_len, len(seen))
            end += 1

        return max_len
        
        # TC: O(N)
        # SC: O(N)


            