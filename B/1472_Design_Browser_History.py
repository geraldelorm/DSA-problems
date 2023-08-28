#Using a dynamic array 
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.curr_page = 0

    def visit(self, url: str) -> None: #tc: O(n) sc: O(n)
        self.pages = self.pages[:self.curr_page + 1]  + [url]
        self.curr_page += 1       

    def back(self, steps: int) -> str: #O(1)
        move_to = self.curr_page - steps
        self.curr_page = max(move_to, 0)

        return self.pages[self.curr_page]

    def forward(self, steps: int) -> str: #O(1)
        move_to = self.curr_page + steps
        self.curr_page = min(move_to, len(self.pages) - 1)

        return self.pages[self.curr_page]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


#Using two stacks
import collections
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = collections.deque([homepage])
        self.forward_history = collections.deque()

    def visit(self, url: str) -> None: #tc: O(1) sc: O(1)
        self.pages.append(url)
        self.forward_history = collections.deque()

    def back(self, steps: int) -> str: #O(n) steps <= n
        while len(self.pages) > 1 and steps:
            self.forward_history.append(self.pages.pop())
            steps -= 1

        return self.pages[-1]

    def forward(self, steps: int) -> str: #O(n) steps <= n
        while self.forward_history and steps:
            self.pages.append(self.forward_history.pop())
            steps -= 1
        
        return self.pages[-1]


#Using a doubly linked list?