class Solution(object):
    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     self.found = False
    #     for i in range(len(board)):
    #         board[i] = list(board[i])
    #
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             self.dfs(i, j, '', board, word)
    #     return self.found
    #
    # def dfs(self, i, j, cur, board, word):
    #     if board[i][j] != word[len(cur)]:  # different value
    #         return
    #
    #     cur += board[i][j]
    #     # use the feature of exclusive or to implement back tracking instead of visited set
    #     # saves memory
    #     # Assumption: board only has ASCII characters
    #     board[i][j] = chr(ord(board[i][j]) ^ 256) # Python 2 should use unichr() instead
    #
    #     if len(cur) == len(word):
    #         self.found = True
    #         return
    #
    #     if self.inbound(board, i, j + 1):
    #         self.dfs(i, j + 1, cur, board, word)
    #     if self.inbound(board, i, j - 1):
    #         self.dfs(i, j - 1, cur, board, word)
    #     if self.inbound(board, i + 1, j):
    #         self.dfs(i + 1, j, cur, board, word)
    #     if self.inbound(board, i - 1, j):
    #         self.dfs(i - 1, j, cur, board, word)
    #
    #     board[i][j] = chr(ord(board[i][j]) ^ 256)
    #
    # def inbound(self, board, i, j):
    #     m, n = len(board), len(board[0])
    #     if i < 0 or i >= m:
    #         return False
    #     if j < 0 or j >= n:
    #         return False
    #     return True

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            board[i] = list(board[i])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, word, 0):
                    return True

        return False

    def dfs(self, i, j, board, word, size):
        # reaching here means all the previous comparison is successful
        if size == len(word):
            return True
        # Deal with out bound case inside dfs
        # Empty-input case included
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return False
        # wrong char
        if board[i][j] != word[size]:
            return False

        board[i][j] = chr(ord(board[i][j]) ^ 256)

        exist = self.dfs(i, j + 1, board, word, size + 1) or \
                self.dfs(i, j - 1, board, word, size + 1) or \
                self.dfs(i + 1, j, board, word, size + 1) or \
                self.dfs(i - 1, j, board, word, size + 1)

        board[i][j] = chr(ord(board[i][j]) ^ 256)

        return exist

# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = 'ABCCED'
board = [
    "ABCE",
    "SFES",
    "ADEE"]
word = "ABCESEEEFS"
print(Solution().exist(board, word))