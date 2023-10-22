class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def build_target(nums, running_sum, i):
            if running_sum > target or i >= len(candidates):
                return
            elif running_sum == target:
                res.append(nums)
            else:
                build_target(nums + [candidates[i]], running_sum + candidates[i], i)
                build_target(nums,running_sum, i + 1)

        for i, v in enumerate(candidates):
            build_target([v], v, i)
        return res


        # TC: O(n*depthOfTree) ~ depth = Total no. of element in candidate // smallest element
        # SC: O(depthOfTree) ~ recursion