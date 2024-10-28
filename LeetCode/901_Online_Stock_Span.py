class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.mono_span_stack = [[float("inf"), 0]]
        
    def next(self, price: int) -> int: #TC: O(N)
        self.stocks.append(price)
        curr_day = len(self.stocks)

        while self.mono_span_stack and self.mono_span_stack[-1][0] <= price:
            self.mono_span_stack.pop()

        last_day = self.mono_span_stack[-1][1]
        span = curr_day - last_day

        self.mono_span_stack.append([price, curr_day])

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)