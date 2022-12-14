# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Input: num1 = "11", num2 = "123"
# Output: "134"

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Input: num1 = "0", num2 = "0"
# Output: "0"


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = "", 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
                
            res = str(carry % 10) + res
            carry = carry // 10
            
        return res
            
# Time O(N)
# Space O(1)