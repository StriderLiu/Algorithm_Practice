# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        height = 0
        left, right = root, root
        while right:
            left, right = left.left, right.right
            height += 1

        if not left: # This tree is full
            return (1 << height) - 1 # "1 << n" equals to "2 ** n"
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2

# O(h ** 2)
print(Solution().countNodes(root))