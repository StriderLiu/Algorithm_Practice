# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        n = 0

        while ptr is not None:
        	n += 1
        	ptr = ptr.next

        for i in range(n - 2, -1, -1):
        	if i is 0:
        		ip = self.position(head, i)
        	else:
        		pre_ip = self.position(head, i)
        		ip = pre_ip.next
        	jp = ip.next

        	while jp is not None:
        		if (jp.next is None and jp.val < ip.val) or (jp.next is not None and jp.next.val > ip.val):
        			if i is 0:
        				head = ip.next
        				ip.next = jp.next
        				jp.next = ip
        				break
        			pre_ip.next = ip.next
        			ip.next = jp.next
        			jp.next = ip
        			break
        		else:
        			jp = jp.next

        return head

    def position(self, head, n):
    	ptr = head
    	for i in range(n - 1):
    		ptr = ptr.next

    	return ptr

if __name__ == '__main__':
	head = ListNode(6)
	node2 = ListNode(3)
	node3 = ListNode(2)
	node4 = ListNode(5)
	node5 = ListNode(4)
	node6 = ListNode(7)
	node7 = ListNode(1)

	head.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6
	node6.next = node7

	node = head
	while node:
		print(node.val)
		node = node.next

	head = Solution().insertionSortList(head)
	print()
	node = head
	while node:
		print(node.val)
		node = node.next;
