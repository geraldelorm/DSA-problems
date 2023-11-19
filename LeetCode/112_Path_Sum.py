# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        runningSum = targetSum - root.val
        if self.isLeaf(root):
            return runningSum == 0
        
        return self.hasPathSum(root.left, runningSum) or self.hasPathSum(root.right, runningSum)
        
    def isLeaf(self, node):
        return not node.left and not node.right

    # TC: O(N)
    # SC: O(logN)