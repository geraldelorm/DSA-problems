# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# s= leetcode -> 0
# s = "loveleetcode" -> 2
# s = "aabb" -> -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}
        
        for c in s:
            lookup[c] = lookup.get(c, 0) + 1
            
        for i, v in enumerate(s):
            if lookup[v] == 1:
                return i
            
        return -1
        
# Time = O(N)
# Space = O(N)