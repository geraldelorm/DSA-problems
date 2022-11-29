# Brute Force
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(self.findOnebits(i))

        return ans

    def findOnebits(self, n: int) -> int:
        total = 0
        while n:
            total += n % 2
            n = n // 2  # logN - this
        return total

# Time = O(NlogN)
# Space = 0(n)

# Using DP


class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            table[i] = 1 + table[i - offset]
        return table

# Time = O(n)
# Space = 0(n)
