class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num == target:
                output.append(i)
        return output
        

# Time O(nlogn)
# Space O(n)