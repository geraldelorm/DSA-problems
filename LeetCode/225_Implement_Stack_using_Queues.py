class MyStack:

    def __init__(self):
        self.queue1 = collections.deque() #append ,popLeft
        self.top_val = None

    def push(self, x: int) -> None: #O(1)
        self.queue1.append(x)
        self.top_val = x   

    def pop(self) -> int: #O(n)
        for _ in range(len(self.queue1) - 1):
            self.top_val = self.queue1.popleft()
            self.queue1.append(self.top_val)

        val = self.queue1.popleft()
        return val

    def top(self) -> int: #O(1)
        return self.top_val

    def empty(self) -> bool: #O(1)
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()