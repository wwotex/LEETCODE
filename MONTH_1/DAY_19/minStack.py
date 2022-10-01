import heapq

class MinStack:

    def __init__(self):
        self.S = []
        self.minS = []

    def push(self, val: int) -> None:
        self.S.append(val)
        val = min(val, self.minS[-1] if self.minS else val)
        self.minS.append(val)

    def pop(self) -> None:
        self.S.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.S[-1]

    def getMin(self) -> int:
        return self.minS[-1]        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()