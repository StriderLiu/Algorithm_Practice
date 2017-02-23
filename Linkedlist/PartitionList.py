# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        left, right = ListNode(0), ListNode(0)
        l, r = left, right
        cur = head
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                r.next = cur
                r = r.next
            cur = cur.next

        r.next = None
        l.next = right.next
        return left.next

node1 = ListNode(2)
node2 = ListNode(1)
node1.next = node2
Solution().partition(node1, 2)