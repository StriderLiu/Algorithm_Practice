# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev, curt = dummy, head
        while curt:
            if curt.val == val:
                prev.next = curt.next
                curt = prev.next
            else:
                prev = curt
                curt = curt.next
        return dummy.next