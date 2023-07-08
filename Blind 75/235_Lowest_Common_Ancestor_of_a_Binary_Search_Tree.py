# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val, p_val, q_val = root.val, p.val, q.val
        
        #if parent if larger than both p and q
        if parent_val > p_val and parent_val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)     
        #if parent if smaller than both p and q
        elif parent_val < p_val and parent_val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
# Time = O(h) ~ height of tree
# Space = O(h) ~ height of tree for recursive calls


# Iterative Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        p_val, q_val = p.val, q.val
        
        while curr:    
            #if parent if larger than both p and q
            if curr.val > p_val and curr.val > q.val:
                curr = curr.left
            #if parent if smaller than both p and q
            elif curr.val < p_val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
        
# Time = O(h) ~ height of tree
# Space = O(1)
