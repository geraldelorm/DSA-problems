#With sorting 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s, t = sorted(s), sorted(t)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
    
# Time = O(nlogn)
# Space = O(1)

#With HashMap 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        map_s, map_t = {}, {}
        
        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1
            
        return map_s == map_t
    
# Time = O(n)
# Space = O(n)


#With Character Count - provided the string contains only ASCII alphabets 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        char_array_s = [0] * 26
        char_array_t = [0] * 26
        
        for i in range(len(s)):
            char_array_s[ord(s[i]) - ord("a")] += 1
            
        for i in range(len(t)):
            char_array_t[ord(t[i]) - ord("a")] += 1
            
        for i in range(26):
            if char_array_t[i] != char_array_s[i]:
                return False
            
        return True
    
# Time = O(n)
# Space = O(1)