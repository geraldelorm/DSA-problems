class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        _min = min(nums)
        _max = max(nums)

        if abs(_max - _min) <= (2 * k):
            return 0

        return abs(_max - _min) - (2*k)

        # tc: O(n)
        # sc: O(1)