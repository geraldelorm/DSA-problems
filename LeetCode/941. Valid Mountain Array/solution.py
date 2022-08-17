class Solution:
    #     def validMountainArray(self, arr: List[int]) -> bool:
    #         if len(arr) < 3:
    #             return False
    #         peek = arr[0]
    #         isNewPeekReached = False

    #         for i in range(1, len(arr)):
    #             if arr[i] == peek:
    #                 return False
    #             elif arr[i] > peek:
    #                 peek = arr[i]
    #             elif arr[i] < peek:
    #                 isNewPeekReached = True
    #             if isNewPeekReached:
    #                 if arr[i] >= peek or arr[i] >= arr[i - 1]:
    #                     return False

    #         return isNewPeekReached == True and peek != arr[0]

    def validMountainArray(self, arr: List[int]) -> bool:
        is_asc = False
        is_desc = False
        for i, item in enumerate(arr):
            if i < len(arr) - 1:
                if arr[i] == arr[i + 1]:
                    return False
                if arr[i] < arr[i + 1]:
                    if is_desc:
                        return False
                    is_asc = True
                if arr[i] > arr[i + 1]:
                    if not is_asc and arr[i] > arr[i + 1]:
                        return False
                    if is_asc and arr[i] < arr[i + 1]:
                        return False
                    is_desc = True
        return is_desc

# Space Complexity = O(1)
# Time Complexity = O(n)
