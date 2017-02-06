import sys
from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # The principle is that in a path graph, the node at the middle is the root with MHTs. Use two pointers to achieve
        # Like course schedule problem. First, construct the graph based on edges. Then construct the degree vector. 
        # Delete all the leaf nodes which the degree is 1. Then construct the next leaf node.
        # Until only two odes are remaining and these two nodes are the two located on the longest path in the graph, which should be the result.
        if n == 0:
            return []
        if n == 1:
            return [0]
        
        result = []
        graph = {x : [] for x in range(n) }
        degree = [0] * n
        
        for li in edges:
            graph[li[0]].append(li[1])
            graph[li[1]].append(li[0])
            degree[li[0]] += 1
            degree[li[1]] += 1
            
        count = n
        while count > 2:
            leaves = []
            
            for i in range(n):
                if degree[i] == 1:
                    leaves.append(i)
                    degree[i] = -1
                    count -= 1
            
            for i in range(len(leaves)):
                for it in graph[leaves[i]]:
                    degree[it] -= 1
            
        for i in range(n):
            if degree[i] == 0 or degree[i] == 1:
                result.append(i)
                    
        return result
        
#         # O(V^2 + VE) algorithm using n times BFS
#         # Store graph in dictionary (linked list)
#         if n == 2:
#             return [0, 1]
#         
#         d = {x : [] for x in range(n) }
#         for li in edges:
#             d[li[0]].append(li[1])
#             d[li[1]].append(li[0])
#         
#         nodes = []
#         for i in d.keys():
#             if len(d[i]) > 1:
#                 nodes.append(i)
#             
#         h, roots, min = [0]*n, [0], sys.maxsize
#         for i in nodes:
#             h[i] = self.bfs(d, i)
#             if h[i] < min:
#                 min = h[i]
#                 roots[0] = i
#         
#         for i in range(n):
#             if h[i] == min and i != roots[0]:
#                 roots.append(i)
#                 
#         return roots
#         
#     def bfs(self, graph, root):
#         queue, visited = deque([root,]), []
#         d, h = [0] * (len(graph.keys())), 0
#         d[root] = 0
#         
#         while queue:
#             node = queue.popleft()
#             
#             if node not in visited:
#                 visited.append(node)
#                 
#             for each in [x for x in graph[node] if x not in visited]:
#                 queue.append(each)
#                 d [each] = d[node] + 1
#                 if d[each] > h:
#                     h = d[each]
#                     
#         return h

n = 2
edges = [[0,1]]
print(Solution().findMinHeightTrees(n, edges))