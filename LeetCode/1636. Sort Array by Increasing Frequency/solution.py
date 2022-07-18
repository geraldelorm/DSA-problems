class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        d=sorted(nums,key=nums.count)
        
        return d 

# TIme O(nlogn)
# Space O(n)