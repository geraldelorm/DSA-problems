#Bruthe Force
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_string = ""
        min_l = float("inf")
        t_map = collections.Counter(t)
        s_map = {}
        l = 0
        
        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            
            while self.contains_all(t_map, s_map):
                if min_l > r - l + 1:
                    sub_string = str(s[l:r + 1])
                min_l = len(sub_string)
                s_map[s[l]] -= 1
                l += 1
        
        return sub_string
    
    def contains_all(self, t_map, s_map):
        for k, v in t_map.items():
            if k in s_map and s_map[k] < v:
                return False
            if k not in s_map:
                return False
        return True
    
    
# Time = O(t * s)
# Space = O(t + s)



# Optimal
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        
        res, res_l = [-1, -1], float("inf")
        t_map, s_map = collections.Counter(t), {}
        
        have, need, l = 0, len(t_map), 0
 
        for r in range(len(s)):
            c = s[r]
            s_map[c] = s_map.get(c, 0) + 1
            
            if c in t_map and s_map[c] == t_map[c]:
                have += 1
            
            while have == need:
                if res_l > (r - l + 1):
                    res = [l, r]
                    res_l = r - l + 1
                s_map[s[l]] = s_map.get(s[l], 0) - 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l: r + 1] if res_l != float("inf") else ""
    
    
# Time = O(n) or O(t + s)
# Space = O(n) 0r O(t + s)