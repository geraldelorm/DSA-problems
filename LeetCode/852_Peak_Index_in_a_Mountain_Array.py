class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        for i in range(1, len(arr) - 1):
            if arr[i -1 ] < arr[i] > arr[i + 1]:
                return i

    # TC: O(n)
    # SC: O(1)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid] < arr[mid - 1]:
                right = mid
            else:
                left = mid + 1


    # TC: O(logN)
    # SC: O(1)