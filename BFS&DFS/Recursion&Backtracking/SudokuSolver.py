class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

    #     self.solve(board)
    #     return
    #
    # def solve(self, board):
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] != '.':
    #                 continue
    #             for num in range(1, 10):
    #                 ch = str(num)
    #                 if self.isValid(board, i, j, ch):
    #                     board[i][j] = ch
    #                     if self.solve(board):
    #                         return True
    #                     else:
    #                         board[i][j] = '.'
    #             return False
    #
    #     return True
    #
    # def isValid(self, board, row, col, ch):
    #     for i in range(0, 9):
    #         if board[row][i] != '.' and board[row][i] == ch:
    #             return False
    #         if board[i][col] != '.' and board[i][col] == ch:
    #             return False
    #         if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
    #                             3 * (col // 3) + i % 3] == ch:
    #             return False
    #     return True

        hashRow = {i: set(list(map(str, range(1, 10)))) for i in range(0, 10)}
        hashCol = {i: set(list(map(str, range(1, 10)))) for i in range(0, 10)}
        hashSq = {}
        for i in range(0, 3):
            for j in range(0, 3):
                hashSq[(3 * i, 3 * j)] = set(list(map(str, range(1, 10))))

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                hashRow[i].discard(board[i][j])
                hashCol[j].discard(board[i][j])
                hashSq[(3 * (i // 3), 3 * (j // 3))].discard(board[i][j])

        self.solve(board, hashRow, hashCol, hashSq)
        return

    def solve(self, board, hashRow, hashCol, hashSq):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    continue
                for num in range(1, 10):
                    ch = str(num)
                    if ch in hashSq[(3 * (i // 3), 3 * (j // 3))] and ch in hashRow[i] and \
                                    ch in hashCol[j]:
                        board[i][j] = ch
                        hashSq[(3 * (i // 3), 3 * (j // 3))].discard(ch)
                        hashRow[i].discard(ch)
                        hashCol[j].discard(ch)
                        if self.solve(board, hashRow, hashCol, hashSq):
                            return True
                        else:
                            board[i][j] = '.'
                            hashSq[(3 * (i // 3), 3 * (j // 3))].add(ch)
                            hashRow[i].add(ch)
                            hashCol[j].add(ch)
                return False

        return True

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
for i in range(len(board)):
    board[i] = list(board[i])
Solution().solveSudoku(board)
print(board)