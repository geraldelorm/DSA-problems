class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True

        return False

# TC: O(n^3)
# SC: O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf

        for v in nums:
            if v <= first:
                first = v
            elif v <= second:
                second = v
            else:
                return True

        return False

# TC: O(n)
# SC: O(1)