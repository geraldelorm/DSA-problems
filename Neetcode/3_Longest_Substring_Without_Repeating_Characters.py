# Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"abcabcbb"
        longest_substring = 0
        
        def isAllUnique(start, end):
            seen = set()
            for i in range(start, end):
                if s[i] in seen:
                    return False
                seen.add(s[i])
            return True
            
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if isAllUnique(i, j):
                    longest_substring = max(longest_substring, j - i)
                       
        return longest_substring
                    
#         TC: O(n^3)
#         SC: O(n)



#OPtinal 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #"abcabcbb"
        longest_substring = 0
        subString = set()
        
        left = 0
        for right in range(len(s)):
            while s[right] in subString:
                subString.remove(s[left])
                left += 1
                
            subString.add(s[right])
            longest_substring = max(longest_substring, len(subString))
                       
        return longest_substring
                    
#         TC: O(n)
#         SC: O(n)
        