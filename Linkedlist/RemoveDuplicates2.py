# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            if not cur.next or (cur.next and cur.next.val != cur.val):
                pre = cur
                cur = cur.next
                continue
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            pre.next = cur.next
            cur = cur.next

        return dummy.next
