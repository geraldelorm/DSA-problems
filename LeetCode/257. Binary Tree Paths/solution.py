# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def findPath(node, path=""):
            if not node.left and not node.right:
                path += str(node.val)
                res.append(path)
                return
            if node.left:
                findPath(node.left, path + str(node.val) + "->")
            if node.right:
                findPath(node.right, path + str(node.val) + "->")
                
            return
            
        findPath(root, "")   
        return res
            
            
# Time O(n)
# Space O(1)