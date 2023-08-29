class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)

        for i in range(end):
            while nums[i] == 0 and i < end - 1:
                j = i
                while j < end - 1:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1

                end -= 1

    # TC: O(N^2)
    # SC: O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # where next non-zero element should be placed 
        index = 0

        for i, v in enumerate(nums):
            if v != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

# TC: O(N)
# SC: O(1)