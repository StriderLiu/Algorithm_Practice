# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue, res = [], []
        node = root
        while node:
            queue.append(node)
            node = node.left
        while queue:
            node = queue.pop()
            res.append(node.val)
            node = node.right
            while node:
                queue.append(node)
                node = node.left
        return res