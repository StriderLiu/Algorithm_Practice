# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s[0] == '(':
            return None

        n, i = len(s), 0
        while i < n:
            if s[i] == '(':
                break
            i += 1
        root = TreeNode(int(s[:i]))

        if i == n:
            return root

        j, counter = i, 0
        while j < n:
            if s[j] == '(':
                counter += 1
            if s[j] == ')':
                counter -= 1
            if counter == 0:
                break
            j += 1
        root.left = self.str2tree(s[i + 1: j])

        if j == n - 1:
            return root

        i = j + 1
        j = i
        j, counter == i, 0
        while j < n:
            if s[j] == '(':
                counter += 1
            if s[j] == ')':
                counter -= 1
            if counter == 0:
                break
            j += 1
        root.right = self.str2tree(s[i + 1: j])
        return root

s = "4(2(3)(1))(6(5))"
print(Solution().str2tree(s).val)

