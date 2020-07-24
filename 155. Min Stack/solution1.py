class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if(self.min > x):
            self.min = x
        

    def pop(self) -> None:
        if (len(self.stack) != 0):
            self.stack.pop()

    def top(self) -> int:
        if(len(self.stack) != 0):
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min in self.stack:
            return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
