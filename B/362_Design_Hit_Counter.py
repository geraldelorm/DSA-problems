#Time scales for when we have multiple hit per second
class HitCounter:

    def __init__(self): #SC: O(n)
        self.hitCount = {}

    def hit(self, timestamp: int) -> None: #TC: O(1)
        self.hitCount[timestamp] = self.hitCount.get(timestamp, 0) + 1
        

    def getHits(self, timestamp: int) -> int: #TC: O(n)
        past5min = timestamp - 300

        count = 0
        for time in self.hitCount:
            if timestamp >= time > past5min:
                count += self.hitCount[time]

        return count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


#Using a queue
class HitCounter:
    def __init__(self):
        self.hits_queue = collections.deque()

    def hit(self, timestamp: int) -> None: #O(1)
        self.hits_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int: #O(n) ~amotized O(1)
        past5mins = timestamp - 300

        while self.hits_queue and self.hits_queue[0] <= past5mins:
            self.hits_queue.popleft()

        return len(self.hits_queue)