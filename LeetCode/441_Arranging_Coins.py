class Solution:
    def arrangeCoins(self, n: int) -> int:
        num_of_rows = 0
        next_row_size = 1

        while n >= next_row_size:
            n -= next_row_size
            next_row_size += 1
            num_of_rows += 1

        return num_of_rows

        # TC: O(n)
        # SC: O(1)


#Using number sesries formular 1, 2, 3, 4......k => (k /2 ) * (k + 1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

        #TC: O(LogN)
        #SC: (1)