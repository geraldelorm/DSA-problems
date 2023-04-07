# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n
        while first < last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            elif not isBadVersion(mid):
                first = mid + 1
        return first

        # O(logN)
