# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node: return True

            if node.val <= low or node.val >= high:
                return False
            
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root)
    
    
# Time O(n)
# Space O(n)



# Iterative Solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, low, high = stack.pop()
            if not node: continue
                
            if node.val <= low or node.val >= high:
                return False
            
            stack.append((node.left, low, node.val)) 
            stack.append((node.right, node.val, high))
        
        return True
    
    
# Time O(n)
# Space O(n)