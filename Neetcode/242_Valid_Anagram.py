# Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    # TC: O(nlogn)
    # SC: O(1)
    
    
# Counting frequency
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in t:
            freq[c] = freq.get(c, 0) - 1
            if freq[c] == 0:
                del freq[c]
             
        return not freq
    
    # TC: O(n)
    # SC: O(n)