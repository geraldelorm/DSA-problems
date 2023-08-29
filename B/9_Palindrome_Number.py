
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        s_x = str(x)
        l, r = 0, len(s_x) - 1

        while l <= r:
            if s_x[l] != s_x[r]: return False
            l += 1
            r -= 1

        return True

        # TC(logN) ~len of x
        # SC: O(1)



# reverse the actual number and compare
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x != 0 and x % 10 == 0: return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = (reversed_num * 10) + x % 10
            x = x // 10

        return original == reversed_num

        # TC(logN) ~len of x
        # SC: O(1)