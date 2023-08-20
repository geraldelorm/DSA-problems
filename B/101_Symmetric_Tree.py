# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not root.left and not root.right: return True

        return self.isMirror(root.left, root.right)


    def isMirror(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False

        return node1.val == node2.val and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

# TC: O(n)
# SC: O(n)