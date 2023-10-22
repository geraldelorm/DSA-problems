class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_val = set(nums1)
        res = set()

        for v in nums2:
            if v in nums1_val:
                res.add(v)

        return list(res)

# TC: O(N + m)
# SC: O(N + m)