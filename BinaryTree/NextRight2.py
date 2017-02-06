# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # O(n) space
    # def connect(self, root):
    #     if not root:
    #         return
    #     toCheck = [root]
    #     while toCheck:
    #         # add next pointer for each node in toCheck
    #         for i in range(len(toCheck) - 1):
    #             toCheck[i].next = toCheck[i + 1]
    #         # update next level nodes sequence
    #         temp = []
    #         for node in toCheck:
    #             if node.left:
    #                 temp.append(node.left)
    #             if node.right:
    #                 temp.append(node.right)
    #         toCheck = temp

    # O(1) space

    # First, cannot use recursion, because it can't control the visit order,
    # right pointers in each level must be all processed before heading to the next level

    # Second, we can only use pointers to simulate visiting by level.
    # root must iterate through "next"
    # keep track of the last node we have processed (prev)
    # use dummy node to save edge checking
    def connect(self, root):
        dummy = TreeLinkNode(0)
        prev = dummy
        while root:
            if root.left:
                prev.next = root.left
                prev = prev.next
            if root.right:
                prev.next = root.right
                prev = prev.next
            root = root.next
            if not root:
                root = dummy.next
                prev = dummy
                # this line seems to be redundant,
                # but it is actually necessary because the loop will never stop without it,
                # consider the scenario in the last level
                dummy.next = None

node1 = TreeLinkNode(1)
node2 = TreeLinkNode(2)
node3 = TreeLinkNode(3)
node4 = TreeLinkNode(4)
node5 = TreeLinkNode(5)
node6 = TreeLinkNode(6)
node7 = TreeLinkNode(7)
node8 = TreeLinkNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node6.right = node8

Solution().connect(node1)

