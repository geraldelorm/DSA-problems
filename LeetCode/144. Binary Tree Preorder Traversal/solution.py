# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def DFS_helper(node, arr = []):
            if node is None:
                return None
            arr.append(node.val)
            DFS_helper(node.left, arr)
            DFS_helper(node.right, arr)
            return arr
            
        return DFS_helper(root)
    

# Time O(n)
# Space O(n)