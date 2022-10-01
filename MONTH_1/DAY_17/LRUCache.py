class LRUCache:

    class ListNode:
        def __init__(self, key, val):
            self.val = val
            self.key = key
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.D = {}
        self.head = None
        self.tail = None
        self.capacity = capacity    
    
    def PRINT(self):
        curr = self.head
        s = 'head:       '
        while curr:
            s += f'{curr.key} -> {curr.val}     '
            curr = curr.next
        print(s)

        
        curr = self.tail
        s = 'tail:       '
        while curr:
            s += f'{curr.key} -> {curr.val}     '
            curr = curr.prev
        print(s)

    def get(self, key: int) -> int:
        # print(f'print(obj.get({key}))')
        if key == 1:
            pass
        if key in self.D:
            node = self.D[key]
            self.toBack(node)
            # self.PRINT()
            return node.val
        else:
            # self.PRINT()
            return -1
    
    def toBack(self, node):
        if self.tail == node:
            return

        
        prev = node.prev
        next = node.next

        if self.head == node:
            self.head = next
            next.prev = None
        else:
            prev.next = next
            next.prev = prev

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

    def put(self, key: int, value: int) -> None:
        # print(f'obj.put({key},{value})')
        if key == 9 and value == 22:
            pass
        # if key already exists -> take node to front and change val
        if key in self.D:
            node = self.D[key]
            node.val = value
            self.toBack(node)
            # self.PRINT()
            return

        # if capacity exceeded -> pop head        
        if len(self.D) == self.capacity:
            self.D.pop(self.head.key)
            self.head = self.head.next
            if self.head: self.head.prev = None

        # create new node and add to dictionary
        new_node = self.ListNode(key, value)
        self.D[key] = new_node

        # add to list
        if len(self.D) == 1:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # self.PRINT()
        
# Your LRUCache object will be instantiated and called as such:
capacity = 10
obj = LRUCache(capacity)

obj.put(10,13)
obj.put(3,17)
obj.put(6,11)
obj.put(10,5)
obj.put(9,10)
print(obj.get(13))
obj.put(2,19)
print(obj.get(2))
print(obj.get(3))
obj.put(5,25)
print(obj.get(8))
obj.put(9,22)
obj.put(5,5)
obj.put(1,30)
print(obj.get(11))
obj.put(9,12)
print(obj.get(7))
print(obj.get(5))
print(obj.get(8))
print(obj.get(9))
obj.put(4,30)
obj.put(9,3)
print(obj.get(9))
print(obj.get(10))
print(obj.get(10))
obj.put(6,14)
obj.put(3,1)
print(obj.get(3))
obj.put(10,11)
print(obj.get(8))
obj.put(2,14)
print(obj.get(1))
print(obj.get(5))
print(obj.get(4))
obj.put(11,4)
obj.put(12,24)
obj.put(5,18)
print(obj.get(13))
obj.put(7,23)
print(obj.get(8))
print(obj.get(12))
obj.put(3,27)
obj.put(2,12)
print(obj.get(5))
obj.put(2,9)
obj.put(13,4)