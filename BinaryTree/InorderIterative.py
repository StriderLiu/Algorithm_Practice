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
        stack, node = [], root
        done = False
        while not done:
            if node:
                stack.append(node)
                node = node.left
            else:
                if stack:
                    node = stack.pop()
                    print(node.val)
                    node = node.right
                else:
                    done = True

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

Solution().inorderTraversal(node1)