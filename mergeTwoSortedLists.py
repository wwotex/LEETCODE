# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode(-69, None)
        curr = head_node
        while list1 is not None or list2 is not None:
            if list1 is None:
                list2, curr = self.addNodeToResult(list2, curr)
            elif list2 is None:
                list1, curr = self.addNodeToResult(list1, curr)
            elif list1.val <= list2.val:
                list1, curr = self.addNodeToResult(list1, curr)
            else:
                list2, curr = self.addNodeToResult(list2, curr)
        

        return head_node.next
    

    def addNodeToResult(self, node, position):
        new_node = ListNode(node.val, None)
        position.next = new_node

        return node.next, position.next

# list1 = [1,2,4]
# list2 = [1,3,4]
# l1 = ListNode(-1, None)
# l2 = ListNode(-1, None)
# for el in list1:
#     new_node = ListNode(el, None)
#     l1.next = 

sol = Solution()
# print(sol.isIsomorphic(l1,l2))