# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        head = None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
            
        p = head
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
                
            p = p.next
            
        if l1:
            p.next = l1
        if l2:
            p.next = l2
            
        return head
    
l1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(19)
node5 = ListNode(20)

l1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

l2 = ListNode(2)
node6 = ListNode(2)
node7 = ListNode(8)
node8 = ListNode(9)
node9 = ListNode(10)

l2.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

head = Solution().mergeTwoLists(l1, l2)

p = head
while p is not None:
    print(p.val)
    p = p.next