# We have n chips, where the position of the ith chip is position[i].
# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.

# Input: position = [1,2,3]
# Output: 1
# Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
# Second step: Move the chip at position 2 to position 1 with cost = 1.
# Total cost is 1.

# Input: position = [2,2,2,3,3]
# Output: 2
# Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.

# Input: position = [1,1000000000]
# Output: 1



class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Its free to move all even position chips together and  all odd position chips together - cost 0      
        even, odd = 0,  0
        N = len(position) #number of coins
        
        for coinsPosition in position:
            if coinsPosition % 2 == 0:
                even += 1
            else:
                odd += 1
                
        print(even, odd)
        # if all chips are in odd or all are in even position - cos will be 0
        if (even == N) or (odd == N): return 0
        
        # else find position(odd or even) with least coins to move
        return min(even, odd)
    
    
#     Time = O(N)
#     Space = O(1)
                
        
        
        