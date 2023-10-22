# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#With Pure Recursion
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start, end):
            if start == end:
                return [TreeNode(start)]
            if start > end:
                return [None]

            generatedTrees = []
            for rootVal in range(start, end + 1):
                for leftTree in generate(start, rootVal - 1):
                    for rightTree in generate(rootVal + 1, end):
                        tree = TreeNode(rootVal, leftTree, rightTree)
                        generatedTrees.append(tree)

            return generatedTrees

        return generate(1, n)


#With caching
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def generate(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start == end:
                return [TreeNode(start)]
            if start > end:
                return [None]

            generatedTrees = []
            for rootVal in range(start, end + 1):
                for leftTree in generate(start, rootVal - 1):
                    for rightTree in generate(rootVal + 1, end):
                        tree = TreeNode(rootVal, leftTree, rightTree)
                        generatedTrees.append(tree)
            
            memo[(start, end)] = generatedTrees
            return generatedTrees

        return generate(1, n)