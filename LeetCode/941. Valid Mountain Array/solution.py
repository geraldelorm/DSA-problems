class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peek = arr[0]
        isNewPeekReached = False
        
        for i in range(1, len(arr)):
            if arr[i] == peek:
                return False
            elif arr[i] > peek:
                peek = arr[i]
            elif arr[i] < peek:
                isNewPeekReached = True
            if isNewPeekReached:
                if arr[i] >= peek or arr[i] >= arr[i - 1]:
                    return False

        return isNewPeekReached == True and peek != arr[0]

# Space Complexity = O(1) 
# Time Complexity = O(n)