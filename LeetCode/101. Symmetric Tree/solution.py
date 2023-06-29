# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, node1, node2): #sameTree leetcode 100
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
        return False        

# Time O(n)
# Space O(1)