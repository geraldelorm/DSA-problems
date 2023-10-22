class MedianFinder:

    def __init__(self): #O(1)
        self.small, self.large = [], [] #maxHeap, minHeap

    def addNum(self, num: int) -> None: #O(logN)
        heapq.heappush(self.small, num * -1)
        
        #balance heaps if: maxHeap ele should be > minHeap ele
        if (self.small and self.large and 
            (self.small[0]  * -1) > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
            
        #balance heap if: size diff > 1
        if(len(self.small) > len(self.large) + 1):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
        if(len(self.large) > len(self.small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float: #O(1)
        if(len(self.small) > len(self.large)):
            return self.small[0] * -1
        if(len(self.large) > len(self.small)):
            return self.large[0]
        return ((self.small[0] * -1) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()