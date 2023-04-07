# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#     Time = O(n)
#     Space = O(n) - worse case non balanced tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_h = self.maxDepth(root.left) + 1
        right_h = self.maxDepth(root.right) + 1

        return max(left_h, right_h)


# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)): # remove all elements at once to increment level only once per level
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return level

#     Time = O(n) not n^2 althogh there is a nested loop
#     Space = O(n)


# NON recursive DFS - we implement our own stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]  # node and depth added to the stack
        level = 0

        while stack:
            curr, depth = stack.pop()
            if curr:
                level = max(level, depth)
                stack.append([curr.left, depth + 1])
                stack.append([curr.right, depth + 1])
        return level
#     Time = O(n)
#     Space = O(n)
