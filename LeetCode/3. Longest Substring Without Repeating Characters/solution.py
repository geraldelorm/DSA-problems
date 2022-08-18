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


# Time O(n) 
# Space O(1)
