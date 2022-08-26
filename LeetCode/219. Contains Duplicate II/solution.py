class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

# Time O(n^2)
# Space O(1)

# Optimal
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for i, v in enumerate(nums):
            if v in lookup.keys() and abs(i - lookup[v]) <= k:
                return True

            lookup[v] = i
        return False

# Time O(n)
# Space O(n)
