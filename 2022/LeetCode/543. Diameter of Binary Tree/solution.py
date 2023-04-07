# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        if root == None:
            return 0
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_h = self.maxDepth(root.left)
        right_h = self.maxDepth(root.right)

        diameter = left_h + right_h
        self.maxDiameter = max(self.maxDiameter, diameter)

        return max(left_h, right_h) + 1
