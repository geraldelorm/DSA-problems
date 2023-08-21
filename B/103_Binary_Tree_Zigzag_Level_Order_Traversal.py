# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        stack1 = collections.deque()
        stack2 = collections.deque()
        res = []

        stack1.append(root)

        while stack1 or stack2:
            firstLevel = []
            while stack1:
                currNode = stack1.pop()
                firstLevel.append(currNode.val)

                if currNode.left:
                    stack2.append(currNode.left)
                if currNode.right:
                    stack2.append(currNode.right)

            if len(firstLevel):   
                res.append(firstLevel)

            secondLevel = []
            while stack2:
                currNode = stack2.pop()
                secondLevel.append(currNode.val)

                if currNode.right:
                    stack1.append(currNode.right)
                if currNode.left:
                    stack1.append(currNode.left)

            if len(secondLevel):
                res.append(secondLevel)

        return res


        # TC: O(N)
        # SC: O(N)
            