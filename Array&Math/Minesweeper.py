class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            board[i] = list(board[i])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.reveal(board, m, n, click[0], click[1])
        return board

    def reveal(self, board, m, n, i, j):
        mines = self.numOfMine(board, m, n, i, j)
        if mines != 0:
            board[i][j] = str(mines)
            return
        else:
            board[i][j] = 'B'
            for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                    if board[x][y] == 'E':
                        self.reveal(board, m, n, x, y)

    def numOfMine(self, board, m, n, i, j):
        cnt = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                if board[x][y] == 'M':
                    cnt += 1
        return cnt

board = ["EEEEE","EEMEE","EEEEE","EEEEE"]
click = [3,0]
print(Solution().updateBoard(board, click))