# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rightSides = []
        visitedLevels = set()
        
        def levelTraversal(node, level):
            if level not in visitedLevels:
                rightSides.append(node.val)
            visitedLevels.add(level)
            
            if node.right:
                levelTraversal(node.right, level + 1)
            
            if node.left:
                levelTraversal(node.left, level + 1)
                
        levelTraversal(root, 0)
        return rightSides
    
    # TC: O(n)
    # SC: (H) ~worse case in unbalanced tree O(n)