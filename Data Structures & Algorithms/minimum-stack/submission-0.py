class MinStack:

    def __init__(self):
        self.minStack = []
        self.miniStack = []
        
    def push(self, val: int) -> None:
       self.minStack.append(val)
       if len(self.miniStack) == 0:
            self.miniStack.append(val)
       elif val < self.miniStack[-1]:
        self.miniStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.miniStack[-1]:
            self.miniStack.pop()
        self.minStack.pop()

        
    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]
        
