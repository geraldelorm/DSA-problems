class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        seen = set()
        
        while right < len(s):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            longest = max(longest, (right - left) + 1)          
            right += 1
            
        return longest
    
#   Time = O(n)
#   Space = O(n)