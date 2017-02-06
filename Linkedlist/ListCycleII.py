# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast, encounter = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                encounter = slow
                break
        if not encounter:
            return None
        # http://blog.csdn.net/wuzhekai1985/article/details/6725263
        while head != encounter:
            head, encounter = head.next, encounter.next
        return head