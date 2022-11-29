# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.stackpush = []
        self.stackdelete = []

    def enqueue(self, ele):
        self.stackpush.append(ele)

    def dequeue(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())

        del self.stackdelete[-1]

    def peek(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())

        return self.stackdelete[-1]


numberOfOperations = int(input())
queue = Queue()

for i in range(numberOfOperations):
    operation = input().split(" ")
    if operation[0] == "1":
        queue.enqueue(int(operation[1]))

    if operation[0] == "2":
        queue.dequeue()

    if operation[0] == "3":
        print(queue.peek())

# Time = O(n)
# Space = O(n)
