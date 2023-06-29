class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        for i in range(length):
            for j in range(length):
                h = min(height[i], height[j])
                distance = j - i
                max_area = max(max_area, h * distance)
        return max_area

# Time O(n^2)
# Space O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        length = len(height)
        left, right = 0, length - 1

        while left < right:
            h = min(height[left], height[right])
            distance = right - left
            max_area = max(max_area, h * distance)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area

# Time O(n)
# Space O(1)
