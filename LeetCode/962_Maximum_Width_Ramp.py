
#Brute force
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    max_width = max(max_width, j - i)

        return max_width

# TC: O(N^2)
# SC: O(1)

# Sorting approach [value, index wise sorting]
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        sorted_nums = []
        for i, v in enumerate(nums):
            sorted_nums.append([v, i])

        sorted_nums.sort( key = lambda x:x[0])

        max_width = 0
        min_val = sorted_nums[0]

        for v, i in sorted_nums:
            if i < min_val[1]:
                min_val = [v, i]

            max_width = max(max_width, i - min_val[1])

        return max_width

# TC: O(nlogn)
# SC: O(n)

# Using two pointer stack
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_max = [None] * len(nums)

        right_max[-1] = nums[-1]

        for idx in range(len(nums) - 2, -1, -1):
            num = nums[idx]
            right_max[idx] = max(num, right_max[idx + 1])

        left, right = 0, 0
        max_width = 0

        while right < len(nums):
            while left < right and nums[left] > right_max[right]:
                left += 1

            max_width = max(max_width, right - left)

            right += 1

        return max_width

# TC: O(N)
# SC: O(N)


#Using monotonic stack
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0

        mono_dec_stack = deque()

        for i, n in enumerate(nums):
            if not mono_dec_stack or mono_dec_stack[-1][0] > n:
                mono_dec_stack.append([n, i])

        i = len(nums) - 1

        while mono_dec_stack and i > 0:
            if nums[i] >= mono_dec_stack[-1][0]:
                max_width = max(max_width, i - mono_dec_stack[-1][1])
                mono_dec_stack.pop()
            else:
                i -= 1

        return max_width
# TC: O(N)
# SC: O(N)