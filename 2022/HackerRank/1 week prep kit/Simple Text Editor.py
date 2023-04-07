class Editor:
    def __init__(self):
        self.S = list()
        self.operationsStack = list()

    def append(self, W): #T = O(1) 
        state = self.S.copy()
        self.S += [i for i in W]
        self.operationsStack.append(state)

    def delete(self, k):  # T = O(1)
        state = self.S.copy()
        while k:
            self.S.pop()
            k -= 1
        self.operationsStack.append(state)

    def printC(self, k):  # T = O(1)
        return self.S[k - 1]

    def undo(self):  # T = O(1)
        prevState = self.operationsStack.pop()
        self.S = prevState

# Space = O(n + n.m) where second n = copy of n saved in stack; where m = number of tracked operations that will grow the stack

numberOfOperations = int(input())
editor = Editor()
for i in range(numberOfOperations):
    operation = input().split()
    if operation[0] == "1":
        editor.append(operation[1])

    if operation[0] == "2":
        editor.delete(int(operation[1]))

    if operation[0] == "3":
        print(editor.printC(int(operation[1])))

    if operation[0] == "4":
        editor.undo()