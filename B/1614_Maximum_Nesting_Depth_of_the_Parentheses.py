class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = 0
        currdepth = 0

        for c in s:
            if c == "(":
                currdepth += 1
            elif c == ")":
                currdepth -= 1

            maxdepth = max(maxdepth, currdepth)

        return maxdepth

        # TC: O(n)
        # SC: O(1)