class Solution:
    def isHappy(self, n: int) -> bool:
        num, seen = n, set()
        while num not in seen:
            seen.add(num)

            num = self.sumOfSquares(num)
            if num == 1:
                return True

        return False

    def sumOfSquares(self, n):
        res = 0

        while n:
            dig = n % 10
            res += dig ** 2
            n = n // 10

        return res

# O(log(N)) -> len of n
# Memory O(N)
