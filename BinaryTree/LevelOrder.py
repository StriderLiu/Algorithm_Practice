from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        res, Q = [], deque()
        Q.append(root)
        size = len(Q)
        
        while Q:
            li = []
            for i in range(size):
                node = Q.popleft()
                li.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(li)
            size = len(Q)
            
        return res