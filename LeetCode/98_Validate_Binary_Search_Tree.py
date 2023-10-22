# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min_val = -math.inf, max_val = math.inf):
            if not root: return True
            if root.val <= min_val or root.val >= max_val:
                return False
        
            return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)

        return validate(root)

        # TC: O(n)
        # SC: O(n)
        