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
