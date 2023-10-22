class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        def twoSum(currPick):
            left, right = currPick + 1, len(nums) - 1

            while left < right:
                threeSum = nums[currPick] + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[currPick], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    #skip dups
                    while left < right and nums[left] == nums[left -1]:
                        left += 1


        nums.sort()

        for currPick in range(len(nums)):
            #avoid duplicates
            if currPick > 0 and nums[currPick] == nums[currPick - 1]:
                continue

            twoSum(currPick)

        return res
    
    # TC: O(n^2)
    # SC: O(n)