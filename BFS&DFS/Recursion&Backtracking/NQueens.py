from copy import deepcopy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(board, row):
            if row == n:
                result.append(['.' * x + 'Q' + '.' * (n - 1 - x) for x in board])
                return
            for x in set_n - set(board):
                # check diagonal conflict
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    dfs(board, row + 1)
                    board[row] = '.'

        result, set_n = [], {i for i in range(n)}
        dfs(['.'] * n, 0)
        return result
        
#         if n == 1:
#             return [['Q']]
#         elif n < 3:
#             return []
#         
#         res = []
#         board = [['.']*n for i in range(n)]
#         self.dfs(res, board, 0)
#         if len(res) is not 0:
#             for board in res:
#                 for i in range(len(board)):
#                     board[i] = ''.join(board[i])
#         return res
#         
#     def dfs(self, res, board, col):
#         if col >= len(board):
#             res.append(deepcopy(board))
#             return
#         
#         for i in range(len(board)):
#             if self.isValid(board, i, col):
#                 board[i][col] = 'Q'
#                 self.dfs(res, board, col + 1)
#                 board[i][col] = '.'
#                 
#     def isValid(self, board, row, col):
#         for i in range(len(board)):
#             for j in range(col):
#                 if board[row][j] == 'Q':
#                     return False
#                 if abs(row - i) == abs(col - j) and board[i][j] == 'Q':
#                     return False
#         
#         return True
    
print(Solution().solveNQueens(4))