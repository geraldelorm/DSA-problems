class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = [i for i in nums1]
        x, i, j = 0, 0, 0
        while i < m and j < n:
            if arr[i] < nums2[j]:
                nums1[x] = arr[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1
            x += 1
            
        while j < n:
            nums1[x] = nums2[j]
            j += 1
            x += 1
            
        while i < m:
            nums1[x] = arr[i]
            i += 1
            x += 1

# Time = O(n)
# Space = O(n)



# Optimal implace
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
