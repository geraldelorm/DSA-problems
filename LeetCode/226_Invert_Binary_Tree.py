# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
# Time = O(n)
# Space = O(h) h = height of the tree

#Iterative Solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        queue = collections.deque([root])
        
        while queue:
            curr = queue.popleft()
            curr.right, curr.left = curr.left, curr.right
            
            if curr.left:
                queue.append(curr.left)
                
            if curr.right:
                queue.append(curr.right)
        
        return root
    
# Time = O(n)
# Space = O(n)