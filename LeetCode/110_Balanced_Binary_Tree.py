# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and (abs(left[1] - right[1]) <= 1))
            
            return [balanced, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]

# Time O(n)
# Space O(1)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        if root == None:
            return True

        self.dfs_height(root)
        return self.answer

    def dfs_height(self, root):
        if root == None or self.answer == False:
            return 0

        left_h = self.dfs_height(root.left)
        right_h = self.dfs_height(root.right)

        if abs(left_h - right_h) > 1:
            self.answer = False

        return max(left_h, right_h) + 1