# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        mid = self.findMid(head)
        node = self.reverse(mid.next)
        while node:
            if head.val != node.val:
                return False
            head, node = head.next, node.next
        return True

    def findMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def reverse(self, head):
        prev, curt = head, head.next
        head.next = None
        while curt:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev