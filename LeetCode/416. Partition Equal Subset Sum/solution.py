class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return 0

        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            newSet = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                newSet.add(t + nums[i])
                newSet.add(t)
            dp = newSet
        return True if target in dp else False

#         total = sum(nums)
#         if total % 2 != 0: return False

#         total = total // 2
#         print(total)

#         dp = [[False] * (total + 1)] * (len(nums) + 1)

#         print(dp)

#         for i in range(len(nums) + 1):
#             dp[i][0] = True

#         for i in range(1, len(nums) + 1):
#             for j in range(1, total + 1):
#                 if j - nums[i - 1] < 0:
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

#         print(dp)
#         return dp[len(nums)][total]
