# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
    #     # O(n) space
    #     self.nodes = []
    #     self.preOrder(root)
    #     for i in range(len(self.nodes) - 1):
    #         self.nodes[i].right = self.nodes[i + 1]
    #         self.nodes[i].left = None
    #
    # def preOrder(self, root):
    #     if not root:
    #         return
    #     self.nodes.append(root)
    #     self.preOrder(root.left)
    #     self.preOrder(root.right)

        # O(1) Space
        if not root:
            return
        curt, next = root, root.right
        while curt.left or curt.right:
            head = curt.left
            if not head:
                curt = next
                next = curt.right
                continue
            tail = self.findTail(head)

            tail.right = next
            curt.right = head
            curt.left = None

            curt = head
            next = curt.right

    def findTail(self, root):
        if not root:
            return None
        while root.right:
            root = root.right
        return root