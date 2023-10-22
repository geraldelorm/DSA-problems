class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        seen = {}
        l = 0
        
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            while ((r - l + 1) - max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1
                
            max_l = max(max_l, r - l + 1)
       
        return max_l
            
# Time = O(n) or O(n * 26) for dictionary lookup for max value
# Space = O(1) or n(26)