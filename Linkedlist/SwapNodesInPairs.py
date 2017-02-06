# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        p = head.next.next
        q = head.next
        
        q.next = head
        head.next = p
        pre = head
        head = q
        
        while p and p.next:
            tmp = p.next.next
            q = p.next
            
            q.next = p
            p.next = tmp
            pre.next = q
            # It is essential to keep the Loop Invariants!!!
            pre = p
            p = tmp
            
        return head
    
node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(6)
node6 = ListNode(2)
node7 = ListNode(2)
  
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

head = Solution().swapPairs(node1)

p = head
while p is not None:
    print(p.val)
    p = p.next