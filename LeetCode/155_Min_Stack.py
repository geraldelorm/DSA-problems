class MinStack:

    def __init__(self):
        self.stack = []    

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            currMin = self.stack[-1][1]
            self.stack.append([val, min(val, currMin)])      

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        # TC (1)
        # SC (n)



#Second solutioin use two stacks 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()