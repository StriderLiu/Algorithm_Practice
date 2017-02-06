# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = [str(root.val)]
        self.bfs(root, res)

        i = -1
        while res[i] == 'N':
            i -= 1

        return ','.join(res[: i + 1])

    def bfs(self, root, res):
        height = self.treeHeight(root)
        level = 1
        toCheck = [root]
        while toCheck:
            tmp = []
            level += 1
            for node in toCheck:
                if node.left:
                    res.append(str(node.left.val))
                    tmp.append(node.left)
                elif level <= height:
                    res.append('N')

                if node.right:
                    res.append(str(node.right.val))
                    tmp.append(node.right)
                elif level <= height:
                    res.append('N')
            toCheck = tmp

    def treeHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')

        root = TreeNode(int(data[0]))
        hash = {0: root}
        start, end = 0, 0
        child = end + 1

        while child < len(data):
            nextStart = child
            for curt in range(start, end + 1):
                if data[curt] == 'N':
                    continue

                if data[child] != 'N':
                    left = TreeNode(int(data[child]))
                    hash[child] = left
                    hash[curt].left = left
                child += 1

                if child >= len(data):
                    break

                if data[child] != 'N':
                    right = TreeNode(int(data[child]))
                    hash[child] = right
                    hash[curt].right = right
                child += 1
            start, end = nextStart, child - 1

        return root

# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# node3 = TreeNode(4)
# node4 = TreeNode(5)
#
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)

root.left = node1
node1.left = node2
node1.right = node3
node3.left = node4

# Your Codec object will be instantiated and called as such:
codec = Codec()
string = codec.serialize(root)
print(string)

newRoot = codec.deserialize(string)
print(codec.serialize(newRoot))