# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if tree is empty or root val is either p or q val return the root ~ we found the LCA
        if root == None or root == p or root == q: return root
        # recursively find LCA in right and left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
# at end of recursion ei at the leaves return the root if values was found in both left & right
# else return the non none node
        if left != None and right != None: return root
        if left != None: return left
        if right != None: return right
    
# Time = O(n)
# Space = O(n)