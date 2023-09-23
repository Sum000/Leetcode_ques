class Stock:
    def __init__(self, price, span):
        self.price = price
        self.span = span
        
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        
        while self.stack and self.stack[-1].price <= price:
            span += self.stack[-1].span
            self.stack.pop()
            
        s = Stock(price, span)
        self.stack.append(s)
        return s.span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)