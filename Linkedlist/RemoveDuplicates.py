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

        prev, curt = head, head.next
        preVal = head.val
        while curt:
            if preVal == curt.val:
                prev.next = curt.next
                curt = prev.next
            else:
                preVal = curt.val
                prev = curt
                curt = curt.next
        return head