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
        # Partial optimization, 
        if head is None or head.next is None: # return special cases
        	return head

        sortedHead = head
        sortedTail = head 
        head = head.next
        sortedHead.next = None

        while head is not None:
        	temp = head;
        	head = head.next
        	temp.next = None

        	# new val is less than the head, just insert in the front
        	if temp.val <= sortedHead.val:
        		temp.next = sortedHead
        		if sortedHead.next is None:
        			sortedTail = sortedHead
        		# sortedTail = sortedHead.next is None ? sortedHead : sortedTail
        		sortedHead = temp
        	elif temp.val >= sortedTail.val:
        		sortedTail.next = temp
        		sortedTail = sortedTail.next
        	else:
        		current = sortedHead
        		while current.next is not None and current.next.val < temp.val:
        			current = current.next

        		temp.next = current.next
        		current.next = temp

        return sortedHead

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