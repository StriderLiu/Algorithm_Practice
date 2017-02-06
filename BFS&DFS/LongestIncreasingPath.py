class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.maxLen = 0
        hash = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in hash:
                    continue
                self.dfs(matrix, i, j, hash)
        return self.maxLen

    def dfs(self, matrix, row, col, hash):
        hash[(row, col)] = 1

        # how to deal with outlet?
        if self.isEnd(matrix, row, col):
            self.maxLen = max(self.maxLen, 1)
            return
        # up
        if row > 0 and matrix[row - 1][col] > matrix[row][col]:
            if (row - 1, col) not in hash:
                self.dfs(matrix, row - 1, col, hash)
            newLen = hash[(row - 1, col)] + 1
            hash[(row, col)] = max(hash[(row, col)], newLen)
            self.maxLen = max(self.maxLen, newLen)
        # down
        if row < len(matrix) - 1 and matrix[row + 1][col] > matrix[row][col]:
            if (row + 1, col) not in hash:
                self.dfs(matrix, row + 1, col, hash)
            newLen = hash[(row + 1, col)] + 1
            hash[(row, col)] = max(hash[(row, col)], newLen)
            self.maxLen = max(self.maxLen, newLen)
        # left
        if col > 0 and matrix[row][col - 1] > matrix[row][col]:
            if (row, col - 1) not in hash:
                self.dfs(matrix, row, col - 1, hash)
            newLen = hash[(row, col - 1)] + 1
            hash[(row, col)] = max(hash[(row, col)], newLen)
            self.maxLen = max(self.maxLen, newLen)
        # right
        if col < len(matrix[0]) - 1 and matrix[row][col + 1] > matrix[row][col]:
            if (row, col + 1) not in hash:
                self.dfs(matrix, row, col + 1, hash)
            newLen = hash[(row, col + 1)] + 1
            hash[(row, col)] = max(hash[(row, col)], newLen)
            self.maxLen = max(self.maxLen, newLen)

    def isEnd(self, matrix, i, j):
        if (not i or matrix[i - 1][j] <= matrix[i][j]) and (
                i == len(matrix) - 1 or matrix[i + 1][j] <= matrix[i][j]) and (
            not j or matrix[i][j - 1] <= matrix[i][j]) and (
                j == len(matrix[0]) - 1 or matrix[i][j + 1] <= matrix[i][j]):
            return True
        return False

matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(Solution().longestIncreasingPath(matrix))