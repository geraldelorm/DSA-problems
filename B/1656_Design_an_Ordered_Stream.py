class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.stream = [None] * n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        
        output = []
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            output.append(self.stream[self.ptr])
            self.ptr += 1

        return output

    # tc: O(n)
    # sc: O(n)


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)