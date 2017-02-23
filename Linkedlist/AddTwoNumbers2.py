# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = self.toNum(l1), self.toNum(l2)
        num = num1 + num2
        l = self.toList(num)
        return self.reverse(l)

    def toNum(self, head):
        cur, num = head, 0
        while cur:
            num = 10 * num + cur.val
            cur = cur.next
        return num

    def toList(self, num):
        head = ListNode(num % 10)
        num = int(num / 10)
        cur = head
        while num:
            cur.next = ListNode(num % 10)
            cur = cur.next
            num = int(num / 10)
        return head

    def reverse(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next = None
        return pre

l1 = ListNode(7)
node11 = ListNode(2)
node12 = ListNode(4)
node13 = ListNode(3)
l1.next = node11
node11.next = node12
node12.next = node13

l2 = ListNode(5)
node21 = ListNode(6)
node22 = ListNode(4)
l2.next = node21
node21.next = node22

Solution().addTwoNumbers(l1, l2)