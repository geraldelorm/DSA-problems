# DP - tabulation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * (len(nums) + 1)
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
                
        return max(lis)
    
    # TC: 0(n^2)
    # SC: O(n)