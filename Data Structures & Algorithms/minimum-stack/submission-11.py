class MinStack:

    def __init__(self):
        self.stack = []        
        self.minstack = []        
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        self.stack.append(val)
        self.minstack.append(self.minVal)

    def pop(self) -> None:
        
        if self.stack and self.minstack:
            self.stack = self.stack[:-1]
            self.minstack = self.minstack[:-1]
            if self.minstack:
                self.minVal = self.minstack[-1]
            else:
                self.minVal = float('inf')


    def top(self) -> int:
        return self.stack[-1]    

    def getMin(self) -> int:
        return self.minstack[-1]

