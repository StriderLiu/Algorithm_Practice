# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Three situations need to be considered:
# 1 What if len(a) <> len(b) ?
# 2 How to deal with the carry ?
# 3 How to deal with the generation of the result licdfest ?
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        node = l3 = None
        carry = 0

        while a or b or (carry == 1):

            if (a is None) and (b is None):
                if l3 is not None:
                    node.next = ListNode(1)
                    node = node.next
                    carry = 0

            elif a is None:
                if (b.val + carry) > 9:
                    if l3 is None:
                        node = l3 = ListNode((b.val + carry) % 10)
                    else:
                        node.next = ListNode((b.val + carry) % 10)
                        node = node.next
                    carry = 1
                else:
                    if l3 is None:
                        node = l3 = ListNode(b.val + carry)
                    else:
                        node.next = ListNode(b.val + carry)
                        node = node.next
                    carry = 0
                b = b.next

            elif b is None:
                if (a.val + carry) > 9:
                    if l3 is None:
                        node = l3 = ListNode((a.val + carry) % 10)
                    else:
                        node.next = ListNode((a.val + carry) % 10)
                        node = node.next
                    carry = 1
                else:
                    if l3 is None:
                        node = l3 = ListNode(a.val + carry)
                    else:
                        node.next = ListNode(a.val + carry)
                        node = node.next
                    carry = 0
                a = a.next

            else:
                if (a.val + b.val + carry) > 9:
                    if l3 is None:
                        node = l3 = ListNode((a.val + b.val + carry) % 10)
                    else:
                        node.next = ListNode((a.val + b.val + carry) % 10)
                        node = node.next
                    carry = 1
                else:
                    if l3 is None:
                        node = l3 = ListNode(a.val + b.val + carry)
                    else:
                        node.next = ListNode(a.val + b.val + carry)
                        node = node.next
                    carry = 0
                a = a.next
                b = b.next
        return l3

if __name__ == '__main__':
    print('List 1:')
    node = l1 = None
    for i in range(1):
        val = int(input())
        if l1 is None:
            node = l1 = ListNode(val)
        else:
            node.next = ListNode(val)
            node = node.next

    print('List 2:')
    node = l2 = None
    for i in range(1):
        val = int(input())
        if l2 is None:
            node = l2 = ListNode(val)
        else:
            node.next = ListNode(val)
            node = node.next

    addition = Solution()
    l3 = addition.addTwoNumbers(l1, l2)

    node = l3
    while node:
        print(node.val)
        node = node.next;
