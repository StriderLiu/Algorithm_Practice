# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.newHead = None
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         if head is None or head.next is None:
#             return head
#         
#         pre = None
#         cur = head
#         next = cur.next    
#         while cur is not None:
#             cur.next = pre
#             pre = cur
#             cur = next
#             if cur:
#                 next = cur.next
#         
#         return pre

        self.helper(None, head, head.next, self.newHead)
        return self.newHead
    
    def helper(self, pre, cur, next, newHead):
        if not cur:
            self.newHead = pre
            return
        
        cur.next = pre
        pre = cur
        cur = next
        if cur:
            next = cur.next
        self.helper(pre, cur, next, newHead)
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
  
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = Solution().reverseList(node1)

p = head
while p is not None:
    print(p.val)
    p = p.next