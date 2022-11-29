class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        lookup1, lookup2 = {}, {}
        
        for i in range(len(s)):
            if s[i] in lookup1.keys():
                lookup1[s[i]] += 1
            else:
                lookup1[s[i]] = 1
                
            if t[i] in lookup2.keys():
                lookup2[t[i]] += 1
            else:
                lookup2[t[i]] = 1
                
        for item in lookup1:
            if not item in lookup2.keys():
                return False
            elif not (lookup1[item] == lookup2[item]):
                return False
            
        return True         

# Time O(n)
# Space O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

# Time O(nlogn)
# Space O(1)
