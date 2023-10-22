# Brute Force
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v == target:
                return i

        return -1
# TIme = O(n)
# Space = O(1)

# Optimal - Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# TIme = O(logN)
# Space = O(1)
