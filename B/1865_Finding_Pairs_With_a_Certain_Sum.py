class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1map = Counter(nums1)
        self.nums2map = Counter(nums2)
        self.nums2 = nums2     

    def add(self, index: int, val: int) -> None:
        self.nums2map[self.nums2[index]] -= 1
        self.nums2[index] = self.nums2[index] + val
        self.nums2map[self.nums2[index]] = self.nums2map.get(self.nums2[index], 0) + 1 

    def count(self, tot: int) -> int:
        pairs = 0
        for valCount in self.nums1map:
            diff = tot - valCount
            if diff in self.nums2map:
               pairs += self.nums2map[diff] * self.nums1map[valCount]

        return pairs
        
# Read the constrains and deside with nums is best to iterate over
# TC: O(1) for count (cap at 1000)
# SC: O(N)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)