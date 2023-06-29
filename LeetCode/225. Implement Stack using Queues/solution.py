class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None: # O(1)
        self.queue.append(x)

    def pop(self) -> int:  # O(n)
        for i in range(len(self.queue) -1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:  # O(1)
        return self.queue[-1]

    def empty(self) -> bool:  # O(1)
        return len(self.queue) == 0


# Good Solution similar to 232. Implement Queue using Stacks