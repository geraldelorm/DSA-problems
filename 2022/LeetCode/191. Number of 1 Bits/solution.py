class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            if n % 2 == 1:  # or simple total += n % 2 (as it either 1 or 0)
                total += 1
            n = n // 2  # bit shift n = n >> 2

        return total

# Time O(n) or technically O(1) -> O(32) cos it's always a 32 bit
# Soace O(1)


# Serious bit manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            total += 1
            n = n & (n-1)  # logic AND
        return total

# Time = O(1)
# Space = O(1)
