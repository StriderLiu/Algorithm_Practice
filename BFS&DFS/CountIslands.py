from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        nRow, nCol = len(grid), len(grid[0])
        islands = []
        for i in range(nRow):
            li = list(grid[i])
            islands.append([int(c) for c in li])

        cnt = 0
        for i in range(nRow):
            for j in range(nCol):
                if not islands[i][j]:
                    continue
                # self.bfs(islands, i, j)
                self.dfs(islands, i, j)
                cnt += 1
        return cnt

    # BFS
    def bfs(self, islands, x, y):
        nRow, nCol = len(islands), len(islands[0])
        que = deque()
        que.append([x, y])
        while que:
            [i, j] = que.popleft()
            if i > 0 and islands[i - 1][j]:  # up
                que.append([i - 1, j])
                islands[i - 1][j] = 0
            if i < nRow - 1 and islands[i + 1][j]:  # down
                que.append([i + 1, j])
                islands[i + 1][j] = 0
            if j > 0 and islands[i][j - 1]:  # left
                que.append([i, j - 1])
                islands[i][j - 1] = 0
            if j < nCol - 1 and islands[i][j + 1]:  # right
                que.append([i, j + 1])
                islands[i][j + 1] = 0

    # DFS
    def dfs(self, islands, x, y):
        if x >= len(islands) or x < 0 or y >= len(islands[0]) or y < 0:
            return
        if islands[x][y]:
            islands[x][y] = 0
            self.dfs(islands, x - 1, y)
            self.dfs(islands, x + 1, y)
            self.dfs(islands, x, y - 1)
            self.dfs(islands, x, y + 1)

grid = ["11000","11000","00100","00011"]
print(Solution().numIslands(grid))