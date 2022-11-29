class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        currSum = float(sum(nums[l:k]))
        maxSum = currSum / k

        for r in range(k, len(nums)):
            currSum += nums[r]
            currSum -= nums[l]
            avg = currSum / k

            maxSum = max(maxSum, avg)

            l += 1

        return maxSum
