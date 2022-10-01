from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = right = dummy
        for x in range(n+1): right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

sol = Solution()
ls_list = [1,2,3,4,5]
n = 5

prehead = curr = ListNode(-1)
for el in ls_list:
    curr.next = ListNode(el)
    curr = curr.next

curr = prehead.next
s = ''
while curr:
    s += ' ' + str(curr.val)
    curr = curr.next
print(s)
new = sol.removeNthFromEnd(prehead.next, n)

curr = new
s = ''
while curr:
    s += ' ' + str(curr.val)
    curr = curr.next
print(s)