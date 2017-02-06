# Given a singly linked list, group all odd nodes together
# followed by the even nodes. Please note here we are talking
# about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in
# O(1) space complexity and O(nodes) time complexity.
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        tail = None
        count = 0
        while ptr:
            if ptr.next is None:
                tail = ptr
            count += 1
            ptr = ptr.next

        ptr = head
        if count > 2:
            for i in range(count//2):
                tail.next = self.deleteNode(ptr)
                tail = tail.next
                ptr = ptr.next

        return head

    def deleteNode(self, ptr):
        tmp = ptr.next
        ptr.next = ptr.next.next
        tmp.next = None
        return tmp

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
#    node7 = ListNode(7)
#    node8 = ListNode(8)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
#    node6.next = node7
#    node7.next = node8

    node = node1
    while node:
        print(node.val)
        node = node.next

    transfer = Solution()
    node1 = transfer.oddEvenList(node1)

    print()
    node = node1
    while node:
        print(node.val)
        node = node.next;