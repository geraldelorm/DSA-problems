#Brute Force ~ sort and return kth element from lastIndex
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# TC: O(nlogn)
# SC: O(n) ~python uses Timsort with can take O(n) space in the worse case



#Brute Force ~ sort in reverse 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]
# TC: O(nlogn)
# SC: O(n) ~python uses Timsort with can take O(n) space in the worse case



# Optimal Space ~ using a heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        largest = None

        for i in range(k):
            largest = heapq.heappop(nums)

        return largest * -1

# TC: O(n) updating values in nums and creating a heap
# SC: O(n) the heap space