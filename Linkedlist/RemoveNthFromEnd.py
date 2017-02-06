# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        
        i, j = head, head
        for m in range(n):
            j = j.next
            
        pre = i
        while j:
            pre = i
            i, j = i.next, j.next
        
        if i == head:
            head = i.next
        else:
            pre.next = i.next
        del i
        return head
    
node1 = ListNode(1)
node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
  
node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

n = 2
p = Solution().removeNthFromEnd(node1, n)
while p is not None:
    print(p.val)
    p = p.next