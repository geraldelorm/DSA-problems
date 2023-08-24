class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        for i in range(len(nums)):
            if ((i == 0 or nums[i - 1] < nums[i]) and
                i == len(nums) -1 or nums[i]  > nums[i + 1]):
                return i

        # TC: O(N)
        # SC: O(1)



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1


        while left < right:
            mid = left + (right - left)//2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1     

        return left

        # TC: O(logN)
        # SC: O(1)