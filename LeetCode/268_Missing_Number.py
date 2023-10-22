# Brute force solution -p actusally faster on leetcode then the rest
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lookup = set()
        for i in nums:
            lookup.add(i)

        for i in range(len(nums) + 1):
            if i not in lookup:
                return i

# Time = O(n) -> 2n
# Space = 0(n)

# class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for i in range(len(nums)):
            sum1 += nums[i]
            sum2 += i
        sum2 += len(nums)
        return sum2 - sum1

# time O(n)
# space O(1)

# Bit manipulation


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res

# time O(n)
# space O(1)
