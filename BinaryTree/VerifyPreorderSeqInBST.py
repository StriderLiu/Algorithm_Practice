class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # O(n) space
        # use stack to simulating iterative inorder traversal
        # utilize the feature of bst: values relationship in each subtree
        # we can simulate the inorder process via comparing the value of each node
        # right > left, right > root
        stack, low = [], float('-inf') # low represents the last visited element
        while curt in preorder:
            if curt < low:
                return False
            while stack and curt > stack[-1]:
                low = stack.pop()
            stack.append(curt)
        return True

        # # O(1) space
        # # use the array from the start as the "stack"
        # # (why? Because as visited elements, they are not important thus can be overwritten)
        # # use i to simulate the top position of stack
        # i, low = -1, float('-inf')
        # for curt in preorder:
        #     if curt < low:
        #         return False
        #     while i >= 0 and curt > preorder[i]:
        #         low = preorder[i]
        #         i -= 1
        #     i += 1
        #     preorder[i] = curt
        # return True