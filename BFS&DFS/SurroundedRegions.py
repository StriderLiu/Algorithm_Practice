from collections import deque

class Solution(object):
    # def solve(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: void Do not return anything, modify board in-place instead.
    #     """
    #     if not board or not board[0]:
    #         return
    #
    #     row, col = len(board), len(board[0])
    #     graph = [[board[i][j] for j in range(col)] for i in range(row)]
    #
    #     # infect all illegal regions lie at left and right border
    #     for i in range(row):
    #         if graph[i][0] == 'O':
    #             self.bfs(graph, i, 0, row, col)
    #         if col > 1 and graph[i][col - 1] == 'O':
    #             self.bfs(graph, i, col - 1, row, col)
    #
    #     # infect all illegal regions lie at top and bottom border
    #     for j in range(1, col - 1):
    #         if graph[0][j] == 'O':
    #             self.bfs(graph, 0, j, row, col)
    #         if row > 1 and graph[row - 1][j] == 'O':
    #             self.bfs(graph, row - 1, j, row, col)
    #
    #     # flip all 'O's into 'X'
    #     # Switch all illegal regions back to 'O's
    #     for i in range(row):
    #         for j in range(col):
    #             if graph[i][j] == 'O':
    #                 continue
    #             graph[i][j] = 'X'
    #
    #
    #     for i in range(row):
    #         for j in range(col):
    #             if graph[i][j] != 'F':
    #                 continue
    #             graph[i][j] = 'O'
    #
    #     # Translate the graph back to board
    #     for i in range(row):
    #         board[i] = ''.join(graph[i])
    #
    # def bfs(self, graph, i, j, row, col):
    #     queue = deque([(i, j)])
    #     while queue:
    #         i, j = queue.popleft()
    #         graph[i][j] = 'F'
    #         # up
    #         if i > 0 and graph[i - 1][j] == 'O':
    #             queue.append((i - 1, j))
    #         # down
    #         if i < row - 1 and graph[i + 1][j] == 'O':
    #             queue.append((i + 1, j))
    #         # left
    #         if j > 0 and graph[i][j - 1] == 'O':
    #             queue.append((i, j - 1))
    #         # down
    #         if j < col - 1 and graph[i][j + 1] == 'O':
    #             queue.append((i, j + 1))

    # Incredibly fast algorithm
    def solve(self, board):
        if not any(board): return

        row, col = len(board), len(board[0])
        # check all four borders
        toCheck = [ij for k in range(row + col) for ij in ((0, k), (row - 1, k), (k, 0), (k, col - 1))]
        graph = [[board[i][j] for j in range(col)] for i in range(row)]
        while toCheck:
            i, j = toCheck.pop()
            # don't care if coordinates in save is legal
            # because they will be constrained
            # we conly select to see those who is legal
            if 0 <= i < row and 0 <= j < col and graph[i][j] == 'O':
                graph[i][j] = 'S'
                toCheck += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j) # put all neighbors in toCheck

        board[:] = [['XO'[c == 'S'] for c in row] for row in graph]

board = ["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"]
# board = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
# board = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"]
# board = ['XXXX','XOOX','XXOX','XOXX']
Solution().solve(board)
print(board)