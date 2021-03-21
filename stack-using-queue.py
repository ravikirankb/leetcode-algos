class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.temp = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.temp = self.stack
        self.stack =[]
        self.stack.append(x)
        for i in self.temp:
            self.stack.append(i)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        val = self.stack[0]
        del self.stack[0]
        return val
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
