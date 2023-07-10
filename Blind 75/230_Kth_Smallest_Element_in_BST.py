# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, output = []):
            if root:
                inorder(root.left, output)
                output.append(root.val)
                inorder(root.right, output)
            return output
        
        return inorder(root)[k - 1]
    
# Time = O(n)
# Space = O(n)


#Iterative Solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        output = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
             
            k -= 1 
            curr = stack.pop()
            if k == 0:
                return curr.val
            curr = curr.right   
    
# Time = O(h + k)
# Space = O(h)
        