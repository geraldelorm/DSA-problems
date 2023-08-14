class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        left = right = 0
        distinct = {}

        while right < len(s):
            distinct[s[right]] = distinct.get(s[right], 0) + 1
            while len(distinct) > k:
                distinct[s[left]] -= 1
                if distinct[s[left]] == 0:
                    del distinct[s[left]]
                left += 1

            max_len = max(max_len, (right - left ) + 1)
            right += 1

        return max_len

        # TC: O(n)
        # SC: O(n)

            