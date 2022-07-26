from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        while curr.next is not None:
            curr, head = self.makeHead(curr, head)
        return head

    
    def makeHead(self, parent, head):
        to_be_head = parent.next
        parent.next = to_be_head.next
        to_be_head.next = head
        return parent, to_be_head




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

L = [1,2,3]

head = list2linked(L)

printLinked(head)
print('\n\n')
printLinked(sol.reverseList(head))       
# print(sol.reverseList(head))