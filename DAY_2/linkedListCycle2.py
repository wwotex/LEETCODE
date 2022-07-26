from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
            
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        D = {}
        index = 0
        curr = head
        while curr is not None:
            if curr in D:
                return curr
            else:
                D[curr] = index
                index += 1
            curr = curr.next
        return None


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

L = [1,2,3,4,5,6]

head = list2linked(L)
head.next.next.next.next.next.next = head.next

# printLinked(head)
# print('\n\n')
print(sol.detectCycle(head))       
# print(sol.reverseList(head))