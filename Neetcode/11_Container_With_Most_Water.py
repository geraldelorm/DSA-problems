class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        for h1 in range(len(height)):
            for h2 in range(h1 + 1, len(height)):
                currArea = (h2 - h1) * min(height[h1], height[h2])
                maxArea = max(maxArea, currArea)
                
        return maxArea
    
    # TC: O(n^2)
    # SC: (1)
    
    
class Solution:
    def maxArea(self, height: List[int]) -> int: #[1,8,6,2,5,4,8,3,7]
        maxArea, left, right = 0, 0, len(height) - 1 
        
        while left < right:
            currArea = (right - left) * min(height[right], height[left])
            maxArea = max(maxArea, currArea)
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
                
        return maxArea
    
    # TC: O(n)
    # SC: (1)