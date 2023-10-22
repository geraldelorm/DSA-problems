# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        
        def height(node):
            if not node: return 0
        
            leftHeight = height(node.left) + 1
            rightHeight = height(node.right) + 1
            
            return max(leftHeight, rightHeight)
        
        return abs(height(root.right) - height(root.left)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    
    # TC: O(n)
    # SC: O(n)