class MyQueue:

    def __init__(self): #space O(N)
        self.enqueue_stack = collections.deque()
        self.dequeue_stack = collections.deque()

    def push(self, x: int) -> None: #O(1)
        self.enqueue_stack.append(x)  

    def pop(self) -> int: #O(1)
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()   

    def peek(self) -> int: #O(1)
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack[-1]

    def empty(self) -> bool: #O(1)
        return not self.enqueue_stack and not self.dequeue_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()