#Brute Force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        def findNextGretestInNums2(n):
            for i, v in enumerate(nums2):
                if n == v:
                    j = i + 1
                    while j < len(nums2):
                        if nums2[j] > v:
                            return nums2[j]
                        j += 1
            return -1


        for v in nums1:
            ans.append(findNextGretestInNums2(v))

        return ans


    # TC: O(n1 * n2)
    # SC: O(n)

#Optimal using a monotonic stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreter = {}

        for i in range(len(nums2) - 1, -1, -1):
            if not stack:
                nextGreter[nums2[i]] = -1
            else:
                while stack and stack[-1] <= nums2[i]:
                    stack.pop()
                if not stack:
                    nextGreter[nums2[i]] = -1
                else:
                    nextGreter[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        res = []
        for n in nums1:
            res.append(nextGreter[n])
        
        return res   



    # TC: O(n1 + n2)
    # SC: O(n)