# Definition for singly-linked list.
import math


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
    def isPalindrome(self, head):
        mid = self.middleNode(head)
        p2 = self.reverseList(mid.next)
        mid.next = p2
        p1 = head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev    


    # cleaner version (wow so cool)
    def middleNode(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    # def middleNode(self, head):
    #     curr = head
    #     length = 0
    #     while curr:
    #         length += 1
    #         curr = curr.next
    #     x = 0
    #     curr = head
    #     mid = (length - 1) // 2
    #     while x < mid:
    #         curr = curr.next
    #         x += 1
    #     return curr            

sol = Solution()
L = []
head = list2linked(L)
printLinked(head)
print('\n')
print(sol.isPalindrome(head))