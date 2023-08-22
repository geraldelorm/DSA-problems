# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]: #O(n)
        #extract content of both trees into an array 
        tree1Vals = self.extractTreeValues(root1, [])
        tree2Vals = self.extractTreeValues(root2, [])

        #merge the two arrays
        i , j, res = 0, 0, [] #0, 1, 1, 2, 3
        while i < len(tree1Vals) and j < len(tree2Vals):
            if tree1Vals[i] < tree2Vals[j]:
                res.append(tree1Vals[i])
                i += 1
            else:
                res.append(tree2Vals[j])
                j += 1

        if i < len(tree1Vals):
            res += tree1Vals[i:]

        if j < len(tree2Vals):
            res += tree2Vals[j:]

        return res


    def extractTreeValues(self, root: TreeNode, output = []) -> List[int]: #O(n)
        if not root: return output

        if root.left:
            self.extractTreeValues(root.left, output) 
        output.append(root.val)

        if root.right:
            self.extractTreeValues(root.right, output) 

        return output


        # TC: O(N + M)
        # SC: O(N + M)

