class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            print(first, second)
            
            if second > first:
                d = (second - first) * -1
                heapq.heappush(stones, d)

        stones.append(0)
        return abs(stones[0])
    
# Time = O(nlog*n)