from ast import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        targetPos = 0
        for pos in range(len(nums)):
            if nums[pos] < target:
                targetPos += 1
            else:
                return pos
        return targetPos

# Time Complexity = O(n)
# Space Complexity = O(1)


# Using Binary search - Divide and Conquer
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r)//2
                
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return l

# Time Complexity = O(logn)
# Space Complexity = O(1)