# Brute force
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def traverse(row, col):
            if row == m and col == n:
                return 1
            if row > m or col > n:
                return 0
            return traverse(row + 1, col) + traverse(row, col + 1)   
            
        return traverse(1, 1)
    
# TC: O(2^n*m)
# SC: O(n*m)


# DP - memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def traverse(row, col, memo): #DFS
            if (row, col) in memo:
                return memo[(row, col)]
            if row > m or col > n:
                memo[(row, col)] = 0
                return 0
            
            memo[(row, col)] = traverse(row + 1, col, memo) + traverse(row, col + 1, memo) 
            return memo[(row, col)]
            
        return traverse(1, 1, {(m, n): 1})
    
# TC: O(n*m)
# SC: O(n*m)