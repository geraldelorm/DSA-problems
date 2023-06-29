# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.



class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0: return 0
        stairs = [1]
        n = n - 1
        
        while n > 0 and n > stairs[-1]:
            new_stair = stairs[-1] + 1
            if n < new_stair:
                return len(stairs)
            stairs.append(new_stair)
            n -= new_stair
            
        return len(stairs)
    
#     Time = O(N)
#     Space = O(N)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0: return 0
        stairs, last_stair = 1, 1
        n = n - 1
        
        while n > 0 and n > last_stair:
            last_stair += 1
            if n >= last_stair: 
                stairs += 1
                n -= last_stair
            
        return stairs
    
# Time = O(N)
# Space = O(1)