# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        slow, fast = head, head
        cnt = 0
        while fast and cnt < k:
            fast = fast.next
            cnt += 1

        # if k > len(list)
        if not fast:
            k %= cnt
            fast, cnt = head, 0
            while fast and cnt < k:
                fast = fast.next
                cnt += 1

        while fast and fast.next:
            slow, fast = slow.next, fast.next

        if not fast:
            return head
        fast.next = head
        newHead = slow.next
        slow.next = None
        return newHead

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
Solution().rotateRight(node1, 3)