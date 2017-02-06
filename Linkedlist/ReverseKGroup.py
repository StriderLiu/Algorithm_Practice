# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # For empty input or linked list with length 1 or step (k) less than 2
        # Return head directly
        if k < 2 or not head or not head.next:
            return head
        
        start, preEnd = head, None
        while True:
            cnt, p = 0, start
            # Find position of end
            while p and cnt < k - 1:
                p = p.next
                cnt += 1
            if not p:
                break
            
            end = p
            # Set the link between previous sub linked list and current sub linked list
            if preEnd:
                preEnd.next = end
            # Next start pointer
            poStart = end.next
            
            # Reverse the sub linked list
            # The key is maintaining the LI
            p = start
            q = p.next
            r = q.next
            while q != poStart:
                q.next = p
                if p is start:
                    p.next = poStart
                p = q
                q = r
                if q != poStart:
                    r = q.next
            
            if start is head:
                head = p
            
            preEnd = start
            start = poStart
            
        return head

k = 3    
h = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

h.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

head = Solution().reverseKGroup(h, k)

p = head
while p is not None:
    print(p.val)
    p = p.next
        
        