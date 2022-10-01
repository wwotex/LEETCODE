class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = [None for x in range(k)]
        self.front = 0
        self.rear = k-1
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear+1)%self.length
            self.Q[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.Q[self.front] = None
            self.front = (self.front+1)%self.length
            return True

    def Front(self) -> int:
        return self.Q[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.Q[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return (self.rear+1)%self.length == self.front and self.Q[self.front] is None

    def isFull(self) -> bool:
        return (self.rear+1)%self.length == self.front and self.Q[self.front] is not None
     
    def print(self):
        print(self.Q)
        print(f'F-> {self.front}   R-> {self.rear}')

obj = MyCircularQueue(3)
for x in range(1,20):
    print('\n\n')
    print(f'\nis full: {obj.isFull()}')
    if x % 5 != 0:
        print(f'\nadd: {obj.enQueue(x)}')
    else:
        print(f'\nremove: {obj.deQueue()}')
    print(f'\nrear: {obj.Rear()}')
    print(f'\nfront: {obj.Front()}')
    obj.print()

