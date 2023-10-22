class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.look_up = OrderedDict()    

    def get(self, key: int) -> int:
        if key in self.look_up:
            val = self.look_up[key]
            del self.look_up[key]
            self.look_up[key] = val
            return val
        else:
            return -1   
    
    def put(self, key: int, value: int) -> None:
        if key in self.look_up:
            self.look_up.pop(key)
        
        if len(self.look_up) >= self.capacity:
            self.look_up.popitem(last=False)
            
        self.look_up[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)