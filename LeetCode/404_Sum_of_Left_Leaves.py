# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def isLeave(node):
            return node.left == None and node.right == None
        
        def leftLeave(node):
            if not node: return 0
            
            if node.left and isLeave(node.left):
                return node.left.val + leftLeave(node.right)
            return leftLeave(node.left) + leftLeave(node.right)
        
        return leftLeave(root)
        
# Time O(n)
# Space O(1)