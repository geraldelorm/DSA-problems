# Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length = 0, 0,  0
        
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                right += 1
                length = max(length, (right - left))
                
        return length
    
# Time = O(n*2) 
# Space = O(n) - making copies of the array during slicing


# Optimal Solution - using a set for lookup

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        left, right, length = 0, 0, 0
        seen = set()
        
        while right < len(s) and left < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                length = max(length, (right - left))
            else:
                seen.remove(s[left])
                left += 1
        return length
    
# Time = O(n) 
# Space = O(n) -set can grow up-to size of the string
