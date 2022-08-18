class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, maxLength = 0, 0, 0, 0
        
        while right < len(s):
            if s[right] in s[left:right]:
                left = left + 1
                length -= 1
            else:
                length += 1
                right += 1
                maxLength = max(length, maxLength)
        return maxLength

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
