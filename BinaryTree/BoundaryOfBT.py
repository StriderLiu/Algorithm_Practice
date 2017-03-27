# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        part1 = [root.val]
        node = root.left
        while node:
            part1.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        n1 = len(part1)
        if n1 > 1:
            part1 = part1[: n1 - 1]

        part2 = []
        self.inorder(root, part2)

        node, part3 = root.right, []
        while node:
            part3.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        n3 = len(part3)
        if n3 > 0:
            part3 = part3[: n3 - 1]
        part3 = self.reverse(part3)

        return part1 + part2 + part3

    def inorder(self, root, part2):
        if not root:
            return
        self.inorder(root.left, part2)
        if not root.left and not root.right:
            part2.append(root.val)
        self.inorder(root.right, part2)

    def reverse(self, li):
        if not li:
            return li
        i, j = 0, len(li) - 1
        while i < j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        return li