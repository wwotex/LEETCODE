from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListMaker:
    def __init__(self, ls_gen):
        prehead = ListNode(-69)
        curr = prehead
        for el in ls_gen:
            curr.next = ListNode(el)
            curr = curr.next
        self.head = prehead.next
    
    def printList(self, head = None):
        if head == None:
            head = self.head
        curr = head
        s = ''
        while curr:
            s += ' ' + str(curr.val)
            curr = curr.next
        print(s)