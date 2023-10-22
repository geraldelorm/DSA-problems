class Logger:

    def __init__(self):
        self.timestamp_map = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timestamp_map:
            self.timestamp_map[message] = timestamp
            return True
        if timestamp - self.timestamp_map[message] >= 10:
            self.timestamp_map[message] = timestamp
            return True
        else:
            return False            
        
# TC: O(1)
# SC: O(M)

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)