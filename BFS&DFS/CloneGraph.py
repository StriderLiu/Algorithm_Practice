from collections import deque

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        # # BFS
        # # The key is old-new hash table, it is also used as "visited"
        # hash, queue = {node: UndirectedGraphNode(node.label)}, deque([node])
        # while queue:
        #     curt = queue.popleft()
        #     for next in curt.neighbors:
        #         if next not in hash:
        #             hash[next] = UndirectedGraphNode(next.label)
        #             queue.append(next)
        #         hash[curt].neighbors.append(hash[next])
        #
        # return hash[node]

            # DFS
            # same idea
            hash = {node: UndirectedGraphNode(node.label)}
            self.dfs(hash, node)
            return hash[node]

        def dfs(self, hash, node):
            if not node:
                return

            for next in node.neighbors:
                if next not in hash:
                    hash[next] = UndirectedGraphNode(next.label)
                    self.dfs(hash, next)
                hash[node].neighbors.append(hash[next])

node = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(3)
node.neighbors = [node2, node3]

print(Solution().cloneGraph(node))