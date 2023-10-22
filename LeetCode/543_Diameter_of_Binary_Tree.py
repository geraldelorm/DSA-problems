# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def depth(root):
            if not root: return 0
            nonlocal diameter
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            
            diameter = max(diameter, left_depth + right_depth)
            
            return max(left_depth, right_depth) + 1
        
        
        depth(root)  
        return diameter
    
    # TC: O(N)
    # SC: O(N)