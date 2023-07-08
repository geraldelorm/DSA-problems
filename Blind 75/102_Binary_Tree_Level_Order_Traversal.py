# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root: return res
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            len_of_q = len(queue)
            level = []
            
            for i in range(len_of_q):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            if level: res.append(level)
                
        return res
        
# Time = O(n)
# Space = O(n)