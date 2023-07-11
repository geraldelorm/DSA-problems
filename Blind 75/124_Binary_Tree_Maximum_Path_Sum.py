# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val #global variable or use array res = [root.val]
        
#         use dfs to find max path spliting only on root 
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
#             update maxval - using curr root plus left and right sum
            self.res = max(self.res, leftMax + rightMax + root.val)
            
            return max(leftMax, rightMax) + root.val
        
        dfs(root)
        return self.res
    
# Time = O(n)
# Space = O(h)
    