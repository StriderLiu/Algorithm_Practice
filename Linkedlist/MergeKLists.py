# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        
        if not n:
            return None
        
        if n == 1:
            return lists[0]
        
        return self.mergeTwo(self.mergeKLists(lists[: int(n / 2)]),
                             self.mergeKLists(lists[int(n / 2) :]))
        
    def mergeTwo(self, h1, h2):
        # Deal with NoneType arguments
        if not h1 and not h2:
            return None
        if not h1:
            return h2
        if not h2:
            return h1
        
        head = None
        if h1.val > h2.val:
            head = h2
            h2 = h2.next
        else:
            head = h1
            h1 = h1.next
            
        p = head
        while h1 and h2:
            if h1.val > h2.val:
                p.next = h2
                p = p.next
                h2 = h2.next
            else:
                p.next = h1
                p = p.next
                h1 = h1.next
                
        if h1:
            p.next = h1
        if h2:
            p.next = h2
            
        return head

# lists = []
#     
# l1 = ListNode(5)
# node1 = ListNode(7)
# node2 = ListNode(9)
# node3 = ListNode(20)
# 
# l1.next = node1
# node1.next = node2
# node2.next = node3
# 
# lists.append(l1)
# 
# l2 = ListNode(3)
# node4 = ListNode(16)
# 
# l2.next = node4
# 
# lists.append(l2)
# 
# l3 = ListNode(2)
# node5 = ListNode(100)
# 
# l3.next = node5
# 
# lists.append(l3)
# 
# l4 = ListNode(1)
# node6 = ListNode(2)
# node7 = ListNode(8)
# 
# l4.next = node6
# node6.next = node7
# 
# lists.append(l4)
# 
# l5 = ListNode(4)
# node8 = ListNode(6)
# node9 = ListNode(10)
# 
# l5.next = node8
# node8.next = node9
# 
# lists.append(l5)

lists = [[], []]

head = Solution().mergeKLists(lists)

p = head
while p is not None:
    print(p.val)
    p = p.next