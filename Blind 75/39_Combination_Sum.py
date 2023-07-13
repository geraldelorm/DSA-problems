class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtracking(arr, total, i):
            if total == target:
                res.append(arr)
                return
            if total > target or i >= len(candidates):
                return 
            
            backtracking(arr + [candidates[i]], total + candidates[i], i)
            backtracking(arr , total, i + 1)
            
                        
        for i, v in enumerate(candidates):
            backtracking([v], v, i)
            
        return res
    
    
#    Time = (N^maxDepth) whre n = number of candidated
#    Space = O(target val / smallest val in candidates)