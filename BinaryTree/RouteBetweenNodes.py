#from enum import Enum
from collections import deque

#class State(Enum):
#	Unvisited = 0
#	Visiting = 1
#	Visited = 2

class Route(object):
	def search(self, graph, start, end):
		if start is end:
			return True

		que = deque([start, ])
		visited = []

		while que:
			node = que.popleft()

			if node not in visited:
				visited.append(node)

			for each in [x for x in graph[node] if x not in visited]:
				if each is end:
					return True
				else:
					que.append(each)

			return False

graph = {
	'A': ['E', 'F'],
	'B': ['C'],
	'C': ['B', 'D'],
	'D': ['C'],
	'E': ['A'],
	'F': ['A']
}

route = Route()

print(route.search(graph, 'B', 'E'))
