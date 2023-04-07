class MyQueue:

    def __init__(self):
        self.stack = []        

    def push(self, x: int) -> None: # O(1)
        self.stack.append(x)

    def pop(self) -> int: # O(n)
        tempStack = self.stack[::-1]
        del self.stack[0]
        return tempStack[-1]     

    def peek(self) -> int: # O(n)
        tempStack = []
        for i in range(len(self.stack) -1,-1,-1):
            tempStack.append(self.stack[i])
        return tempStack[-1]

    def empty(self) -> bool: # O(1)
        return len(self.stack) == 0
        

# Time Complexity of most operations = O(n) and O(n) Space complexity as well


# Batter Solution with data duplication in both stacks 
class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverseStack = []

    def push(self, x: int) -> None: # O(n) due to insertion at index 0 requires shifting
        self.stack.append(x)
        self.reverseStack.insert(0, x)

    def pop(self) -> int: # O(1) approximately
        val = self.reverseStack[-1]
        del self.stack[0]
        del self.reverseStack[-1]
        return val    

    def peek(self) -> int: # O(1)
        val = self.reverseStack[-1]
        return val

    def empty(self) -> bool: # O(1)
        return len(self.stack) == 0
        


# OR

# Better Solution that avoids duplication in both stacks
class MyQueue:
    #T=O(1) amortized
    #S=O(n)
    def __init__(self):
        self.inStack  = []
        self.outStack = []

    #T=O(1), S=O(n)
    def push(self, x: int) -> None:
        self.inStack.append(x)

    #T=O(1) amortized, S=O(1)
    def pop(self) -> int:
        self.move()
        return self.outStack.pop()

    #T=O(1) amortized, S=O(1)
    def peek(self) -> int:
        self.move()
        return self.outStack[-1]
    
    #T=O(1), S=O(1)
    def empty(self) -> bool:
        return not self.inStack and not self.outStack
    
    def move(self) -> None:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())



class MyQueue:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None: # O(1)
        self.stack.append(x)

    def pop(self) -> int: # O(n)
        for i in range(len(self.stack) -1):
            self.stack.insert(0, (self.stack.pop()))
        return self.stack.pop()

    def peek(self) -> int: # O(1)
        return self.stack[0]

    def empty(self) -> bool: # O(1)
        return len(self.stack) == 0
