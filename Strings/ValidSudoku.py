class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            tab = {'1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1}
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                tab[board[i][j]] -= 1
                if tab[board[i][j]] < 0:
                    return False
                
        for i in range(0, 9):
            tab = {'1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1}
            for j in range(0, 9):
                if board[j][i] == '.':
                    continue
                tab[board[j][i]] -= 1
                if tab[board[j][i]] < 0:
                    return False
                
        for i in range(0, 3):
            for j in range(0, 3):
                tab = {'1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1}
                r, c = i*3, j*3
                for k in range(0, 3):
                    for l in range(0, 3):
                        if board[r+k][c+l] == '.':
                            continue
                        tab[board[r+k][c+l]] -= 1
                        if tab[board[r+k][c+l]] < 0:
                            return False
                        
        return True

board = [".87654321",
         "2........",
         "3........",
         "4........",
         "5........",
         "6........",
         "7........",
         "8........",
         "9........"]
print(Solution().isValidSudoku(board))