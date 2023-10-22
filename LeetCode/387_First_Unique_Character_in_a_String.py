class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1

        # tc: O(n)
        # sc: O(1) cos s contains only lowercase englist chars the count table will be 26 max