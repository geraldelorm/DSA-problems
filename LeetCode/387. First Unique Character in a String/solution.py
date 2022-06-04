# Liner Time Solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        
# T = 0(n) = counter uses a hashmap 
# S = O(1)  because the string can only have 26 unique characters in the map


# Other Solution  implementing out own lookup table
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {} 
        for c in s: 
            if (c in lookup): 
                lookup[c] += 1
            else: 
                lookup[c] = 1
        
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i
        return -1
        
# T = 0(n) = counter uses a hashmap 
# S = O(1) because the string can only have 26 unique characters in the map