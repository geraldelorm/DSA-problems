# Brute force
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        min_swaps = len(nums)
        ones = nums.count(1)
        nums += nums

        l = 0
        r = ones

        while r < len(nums):
            currSwap = nums[l:r].count(0)
            min_swaps = min(min_swaps, currSwap)

            l += 1
            r += 1
        
        return min_swaps
# Time = O(n^2) Space = O(n)


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        min_swaps = len(nums)
        ones = nums.count(1)
        zeros = nums[:ones].count(0)
        nums += nums

        for i in range(ones, len(nums)):
            min_swaps = min(min_swaps, zeros)
            if nums[i] == 0:
                zeros += 1

            if nums[i - ones] == 0:
                zeros -= 1
        
        return min_swaps

# O(n)
