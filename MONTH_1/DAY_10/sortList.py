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
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        mid = self.middleNode(head)
        h2 = mid.next
        mid.next = None 
        h1 = self.sortList(head)
        h2 = self.sortList(h2)
        return self.merge(h1, h2)


    def middleNode(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, h1, h2):
        prehead = ListNode(-69)
        curr = prehead
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        while h1:
            curr.next = h1
            h1 = h1.next
            curr = curr.next
        while h2:
            curr.next = h2
            h2 = h2.next
            curr = curr.next
        return prehead.next


sol = Solution()
L = [-1,5,3,4,0]
head = list2linked(L)
printLinked(head)
print('\n')

printLinked(sol.sortList(head))