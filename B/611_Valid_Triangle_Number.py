#Brute Force
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        def isValidTriangle(firstSide, secondSide, ThridSide):
            if ((firstSide + secondSide) > ThridSide and 
                (firstSide + ThridSide) > secondSide and 
                (secondSide + ThridSide) > firstSide):
                return True
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if isValidTriangle(nums[i], nums[j], nums[k]):
                        res += 1

        return res

        # TC: O(n^2)
        # SC: O(1)

#Optimal ~ With Sorting
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i + 1, len(nums)):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    res += k - j - 1

        return res

        # TC: O(n^2)
        # SC: O(1)