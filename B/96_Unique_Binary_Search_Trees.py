class Solution:
    def numTrees(self, n: int) -> int:
        numOfTrees = [1] * (n + 1)
        
        for node in range(2, n + 1):
            trees = 0
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                #number of unique subtree on left and right
                trees += numOfTrees[left] * numOfTrees[right]
            numOfTrees[node] = trees
            
        return numOfTrees[n]
    
    # TC: O(n^2)
    # SC: O(N)