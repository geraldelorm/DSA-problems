class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        res = []
        p_map, s_map = collections.Counter(p), {}
        
        l = 0
        
        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            if r - l == len(p) - 1:
                if self.compare_maps(s_map, p_map):
                    res.append(l)
                
                s_map[s[l]] = s_map.get(s[l], 0) - 1
                l += 1  
        
        return res
    
    def compare_maps(self, s_map, p_map):
        for k in p_map:
            if k not in s_map:
                return False
            elif s_map[k] != p_map[k]:
                return False
    
        return True
    
    
# Time = O(S)
# Space = O(1) - map will have 26 chars max