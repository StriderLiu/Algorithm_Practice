# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        (pre, mid) = self.findMid(head)
        root = TreeNode(mid.val)

        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def findMid(self, head):
        if not head:
            return (None, None)

        slow, fast = head, head.next
        pre = None
        while fast and fast.next:
            pre = slow
            slow, fast = slow.next, fast.next.next
        return (pre, slow)