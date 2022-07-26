from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = self.linked2list(head)
        mid_val = ls[ int(len(ls)/2) ]
        return mid_val
    
    def linked2list(self, head):
        ls = []
        curr = head
        while curr is not None:
            ls.append(curr)
            curr = curr.next
        return ls




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

L = [1,2,3,4,5, 6]

head = list2linked(L)

printLinked(head)
print('\n\n')
print(sol.middleNode(head).val)       
# print(sol.reverseList(head))