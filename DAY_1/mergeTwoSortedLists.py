# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

#cleaner solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-69)
        curr = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if not list2 else list2
        return prehead.next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head_node = ListNode(-69, None)
#         curr = head_node
#         while list1 is not None or list2 is not None:
#             if list1 is None:
#                 list2, curr = self.addNodeToResult(list2, curr)
#             elif list2 is None:
#                 list1, curr = self.addNodeToResult(list1, curr)
#             elif list1.val <= list2.val:
#                 list1, curr = self.addNodeToResult(list1, curr)
#             else:
#                 list2, curr = self.addNodeToResult(list2, curr)
        

#         return head_node.next
    

#     def addNodeToResult(self, node, position):
#         new_node = ListNode(node.val, None)
#         position.next = new_node

#         return node.next, position.next

# list1 = [1,2,4]
# list2 = [1,3,4]
# l1 = ListNode(-1, None)
# l2 = ListNode(-1, None)
# for el in list1:
#     new_node = ListNode(el, None)
#     l1.next = 

sol = Solution()
# print(sol.isIsomorphic(l1,l2))