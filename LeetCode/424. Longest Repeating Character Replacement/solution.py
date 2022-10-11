class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size = 0
        left = 0
        seen = {}

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1

            if (right - left + 1) - max(seen.values()) <= k:
                max_size = max(max_size, (right - left + 1))
            else:
                seen[s[left]] -= 1
                left += 1

        return max_size


# time /space = O(n)
