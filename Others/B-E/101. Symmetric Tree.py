# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# E.g

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Approach
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.sameTree(root.right, root.left)

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.sameTree(root1.left, root2.right) and self.sameTree(root1.right, root2.left)

# Time O(N)
# Space O(N)


#Iterative approach
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = collections.deque()
        stack.append((root.right, root.left))

        res = True
        while stack:
            root1, root2 = stack.pop()

            if root1 and root2 and (root1.val == root2.val):
                stack.append((root1.left, root2.right))
                stack.append((root1.right, root2.left))
            elif not root1 and not root2:
                continue
            else:
                res = False
                break

        return res
# Time O(N)
# Space O(N)
