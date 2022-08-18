# Definition for singly-linked list.
from ast import Pass
from email import header


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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



class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None
        dest = head
        origin = head.next
        while origin and origin.next:
            self.move(origin, dest)
            origin = origin.next
            dest = dest.next
        return head
        


    
    def move(self, origin, dest):
        to_move = origin.next
        origin.next = origin.next.next
        to_move.next = dest.next
        dest.next = to_move


sol = Solution()
L = [1,2,3,4,5,6]
head = list2linked(L)
printLinked(head)
print('\n')

printLinked(sol.oddEvenList(head))