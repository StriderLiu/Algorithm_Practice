# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        toDel, toDelParent = root, None
        while toDel and toDel.val != key:
            toDelParent = toDel
            if key < toDel.val:
                toDel = toDel.left
            elif key > toDel.val:
                toDel = toDel.right

        if not toDel:
            return root

        newRoot = root
        replace, parent = toDel.right, None
        while replace and replace.left:
            parent = replace
            replace = replace.left

        if replace:  # find the first node larger than toDel (right, left, left, ...)
            if parent:
                replaceRight = replace.right
                parent.left = replaceRight
                replace.left, replace.right = toDel.left, toDel.right
            else:
                replace.left = toDel.left

        elif toDel.left:  # replace with the left child
            replace = toDel.left

        if not toDelParent:  # toDel is root
            newRoot = replace
        elif toDel is toDelParent.left:
            toDelParent.left = replace
        else:
            toDelParent.right = replace

        return newRoot

node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(2)

node1.left = node2
node1.right = node3
node2.right = node4

Solution().deleteNode(node1, 0)