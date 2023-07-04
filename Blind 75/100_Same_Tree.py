# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        elif not q or not p:
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        
# Time = O(n)
# Space = O(n) ~ worse case

# Iterative
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q: 
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        queue = collections.deque([(p, q),])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p or q:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))        
            
        return True
        
# Time = O(n)
# Space = O(n) ~ worse case