# Brute Force
from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] == target - nums[y]:
                    return [x, y]

# Time Complexity O(n^2)
# Space complexity O(1)


# Optimization using a map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in lookup:
                return [lookup[diff], index]
            lookup[value] = index

# Time Complexity O(n)
# Space complexity O(n)