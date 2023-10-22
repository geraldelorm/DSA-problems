class KthLargest:

    def __init__(self, k: int, nums: List[int]): #0(nlog*n)
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int: #0(log*n)
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        return self.minHeap[0] #0(1)
        
# Space = O(n)