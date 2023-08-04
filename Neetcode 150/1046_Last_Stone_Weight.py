class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, (s * -1))
        
        while len(heap) > 1:
            first_stone = heapq.heappop(heap) * -1
            second_stone =  heapq.heappop(heap) * -1
            
            if first_stone != second_stone:
                new_stone = first_stone - second_stone
                heapq.heappush(heap, (new_stone * -1))   
            
        
        return heap[0] * -1 if len(heap) > 0 else 0
        
        # TC: O(NLogN)
        # SC: O(n)