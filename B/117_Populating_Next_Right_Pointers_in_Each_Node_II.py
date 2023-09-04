"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            curr_level_len = len(queue)

            for i in range(curr_level_len):
                node = queue.popleft()

                if i < curr_level_len - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root

        # TC: O(n)
        # SC: O(n)