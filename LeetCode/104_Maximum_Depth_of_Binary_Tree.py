# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
    
# Time = O(n)
# Space = O(h) ~logN


# Iterative SO=olution with a stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is None: 
            return 0
        
        stack.append((1, root))  
        depth = 0
        
        while len(stack) > 0:
            curr_depth, curr_node = stack.pop()
            if curr_node:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, curr_node.left))
                stack.append((curr_depth + 1, curr_node.right))

        return depth
        
    
# Time = O(n)
# Space = O(n)~ woorse case -> logN ~ average case