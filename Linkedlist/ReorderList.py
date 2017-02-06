# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        mid = self.findMid(head)
        right = self.reverse(mid.next)
        mid.next = None
        self.merge(head, right)

    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def reverse(self, head):
        prev, curt = head, head.next
        prev.next = None
        while curt:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev

    def merge(self, left, right):
        dummy = ListNode(0)
        curt = dummy
        while right:
            curt.next = left
            left, curt = left.next, curt.next
            curt.next = right
            right, curt = right.next, curt.next
        curt.next = left
        return dummy.next