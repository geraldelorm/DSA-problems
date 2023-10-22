class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        new_set = set()
        for j in jewels:
            new_set.add(j)
            
        count = 0
        for stone in stones:
            if stone in new_set:
                count += 1
        return count

# Time Complexity = O(n) - n + m (jewels and stones)
# Space Complexity = O(n) 