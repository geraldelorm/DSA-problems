class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length = 0, 0, 0
        
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                right += 1
                length = max(length, right - left)
        return length

# Time O(n) or possibly n^2 our substring s[left: right] could take O(n) to search 
# Space O(1)



# Using hashmap to reduce lookup/search time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start, end, length = 0, 0, 0
        seen = set()

        while start < len(s) and end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                length = max(length, end - start)
            else:
                seen.remove(s[start])
                start += 1
        return length

# Time O(n) 
# Space O(1)
