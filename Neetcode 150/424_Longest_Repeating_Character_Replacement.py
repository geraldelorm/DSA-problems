class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_substring = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            #check that the current windows is valid 
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

            longest_substring = max(longest_substring, (r - l + 1))

        return longest_substring
    
    # tc: O(n * 26) ~ 26 for geting dictionary max
    # sc: O(n)

