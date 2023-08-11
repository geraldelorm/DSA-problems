class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

        # TC: O(n)
        # SC: O(n)

