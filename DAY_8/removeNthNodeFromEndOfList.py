# Definition for singly-linked list.
from email import header
from tkinter import N


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        prehead = ListNode(-69)
        prehead.next = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = length - n
        curr = prehead
        i = 0
        while i < k:
            curr = curr.next
            i += 1
        curr.next = curr.next.next

        return prehead.next
    
sol = Solution()

def list2linked(ls):
    curr = dummy = ListNode(-69, None)
    for el in ls:
        curr.next = ListNode(el, None)
        curr = curr.next
    return dummy.next

def printLinked(head):
    print('linked list: ')
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
    print('\n')

L = [1,2,3,4,5]

head = list2linked(L)
n = 5

printLinked(head)
print('\n\n')
printLinked(sol.removeNthFromEnd(head, n))      