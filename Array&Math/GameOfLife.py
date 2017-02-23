class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        # transfer
        for i in range(m):
            for j in range(n):
                liveNei = self.countLive(board, i, j, m, n)
                if board[i][j] and (liveNei == 2 or liveNei == 3):
                    board[i][j] = 3
                if not board[i][j] & 1 and liveNei == 3:
                    board[i][j] = 2
        # recover
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    # count the # of live neighbors
    def countLive(self, board, i, j, m, n):
        cnt = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                cnt += board[x][y] & 1
        cnt -= board[i][j] & 1
        return cnt

board = [[1,1],[1,0]]
Solution().gameOfLife(board)
print(board)