# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return 1 + self.maxDepth(root.right)
        elif not root.right:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
root = TreeNode(4)
node1 = TreeNode(3)
node2 = TreeNode(1)

root.left = node1
root.right = node2

node3 = TreeNode(6)
node4 = TreeNode(7)

node1.left = node3
node1.right = node4

node5 = TreeNode(8)

node2.right = node5

node6 = TreeNode(9)

node5.left = node6

print(Solution().maxDepth(root))