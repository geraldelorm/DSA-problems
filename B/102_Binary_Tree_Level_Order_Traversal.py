# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        queue.append(None)

        while queue and queue[0]:
            curr_node = queue.popleft()
            curr_level = []

            while curr_node:
                curr_level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

                curr_node = queue.popleft()

            res.append(curr_level)
            queue.append(None)

        return res

        # TC: O(N)
        # SC: O(N)
