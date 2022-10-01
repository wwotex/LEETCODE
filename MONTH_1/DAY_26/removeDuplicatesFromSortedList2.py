# Definition for singly-linked list.
from typing import Optional
from ListManager import ListNode, ListMaker

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-101)
        prehead.next = head
        prev, curr = prehead, head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next


        return prehead.next

sol = Solution()
ls = [1,1,1,2,2]
gen = ListMaker(ls)
gen.printList()
res =  sol.deleteDuplicates(gen.head)
if res:
    gen.printList(res)