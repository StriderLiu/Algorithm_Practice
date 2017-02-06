# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode(-1)
        if left.val < right.val:
            dummy.next = left
            left = left.next
        else:
            dummy.next = right
            right = right.next
        curt = dummy.next
        while left and right:
            if left.val < right.val:
                curt.next = left
                left = left.next
            else:
                curt.next = right
                right = right.next
            curt = curt.next
        if left:
            curt.next = left
        else:
            curt.next = right
        return dummy.next