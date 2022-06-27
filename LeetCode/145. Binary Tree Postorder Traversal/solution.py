# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node, arr = []):
            if node is None:
                return None
            helper(node.left, arr)
            helper(node.right, arr)
            arr.append(node.val)
            
            return arr

        return helper(root)

# Time O(n)
# Space O(n)