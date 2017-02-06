from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, Q = [], deque()
        Q.append(root)
        size, goLeft = len(Q), False
        while Q:
            li= []
            for i in range(size):
                node = Q.popleft()
                if goLeft:
                    li = [node.val] + li
                else:
                    li.append(node.val)
                    
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            
            if not goLeft:
                goLeft = True
            else:
                goLeft = False
            res.append(li)
            size = len(Q)
        
        return res
    
root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

print(Solution().zigzagLevelOrder(root))