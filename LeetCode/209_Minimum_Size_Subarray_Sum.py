class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        left = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_size = min(min_size, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_size if min_size != float("inf") else 0

# Space complexity: O(1)
# Time complexity: O(n)