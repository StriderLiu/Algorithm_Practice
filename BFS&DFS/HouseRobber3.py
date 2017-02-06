# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # # version 1: naive solution
        # if not root:
        #     return 0
        # val = 0
        # if root.left:
        #     val += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     val += self.rob(root.right.left) + self.rob(root.right.right)
        # return max(val + root.val, self.rob(root.left) + self.rob(root.right))

    #     # version 2: use DP way to eliminate duplications
    #     hash = {}
    #     return self.robSub(root, hash)
    #
    # def robSub(self, root, hash):
    #     if not root:
    #         return 0
    #     if root in hash:
    #         return hash[root]
    #     val = 0
    #     if root.left:
    #         val += self.robSub(root.left.left, hash) + self.robSub(root.left.right, hash)
    #     if root.right:
    #         val += self.robSub(root.right.left, hash) + self.robSub(root.right.right, hash)
    #     val = max(val + root.val, self.robSub(root.left, hash) + self.robSub(root.right, hash))
    #     hash[root] = val
    #     return val

        # version 3: eliminate duplicate subproblems at the very beginning -- redefine rob(root)
        # seperate the 2 different scenarios
        res = self.robSub(root)
        return max(res[0], res[1])

    def robSub(self, root):
        if not root:
            # (!rob, rob)
            return (0, 0)
        left, right = self.robSub(root.left), self.robSub(root.right)
        val1 = max(left[0], left[1]) + max(right[0], right[1])
        val2 = root.val + left[0] + right[0]
        return (val1, val2)

root = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2

node3 = TreeNode(3)
node4 = TreeNode(1)

node1.right = node3
node2.right = node4

print(Solution().rob(root))