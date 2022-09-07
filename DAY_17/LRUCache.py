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
    
    def print(self):
        curr = self.head
        s = 'head:       '
        while curr:
            s += f'{curr.key} -> {curr.val}     '
            curr = curr.next
        print(s)

    def get(self, key: int) -> int:
        print(f'get: {key}')
        if key in self.D:
            node = self.D[key]
            self.toBack(node)
            self.print()
            return node.val
        else:
            self.print()
            return -1
    
    def toBack(self, node):
        if self.tail == node:
            return

        
        prev = node.prev
        next = node.next

        if self.head == node:
            self.head = next
        else:
            prev.next = next

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

    def put(self, key: int, value: int) -> None:
        print(f'put: {key}')
        # if key already exists -> take node to front and change val
        if key in self.D:
            node = self.D[key]
            node.val = value
            self.toBack(node)
            self.print()
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
        self.print()
        
# Your LRUCache object will be instantiated and called as such:
capacity = 10
obj = LRUCache(capacity)

obj.put(2,1)
print(obj.get(2))
obj.put(3,2)
print(obj.get(2))
print(obj.get(3))