# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def refill(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.refill(node.right)
        return node.val

root = TreeNode(3)
node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(2)

root.left = node1
root.right = node2
node1.right = node3

# Your BSTIterator will be called like this:
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print(v)