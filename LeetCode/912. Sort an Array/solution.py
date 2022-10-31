from heapq import heapify, heappop
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        firstHalf = nums[:mid]
        secondHalf = nums[mid:]

        firstHalf = self.sortArray(firstHalf)
        secondHalf = self.sortArray(secondHalf)

        return self.merge(firstHalf, secondHalf)

    def merge(self, arr1, arr2):
        newArray = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                newArray.append(arr1[i])
                i += 1
            else:
                newArray.append(arr2[j])
                j += 1

        while i < len(arr1):
            newArray.append(arr1[i])
            i += 1

        while j < len(arr2):
            newArray.append(arr2[j])
            j += 1

        return newArray

        # O(NlogN)



# Heap Sort O(NlogN)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build max heap
        for i in range(n//2, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            # Swap
            nums[i], nums[0] = nums[0], nums[i]

            # Heapify root element
            self.heapify(nums, i, 0)

        return nums

    def heapify(self, arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)


# SImple with builth in heapq


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapify(nums)

        newarr = []

        for i in range(n):
            newarr.append(heappop(nums))

        return newarr
