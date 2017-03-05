class Solution(object):
    # Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []

        matrix = [[0 for j in range(n)] for i in range(n)]
        matrix[0][0], cnt, i, j = 1, 1, 0, 0
        while cnt < n ** 2:
            # right
            while j < n - 1 and not matrix[i][j + 1]:
                j += 1
                cnt += 1
                matrix[i][j] = cnt

            # down
            while i < n - 1 and not matrix[i + 1][j]:
                i += 1
                cnt += 1
                matrix[i][j] = cnt

            # left
            while j > 0 and not matrix[i][j - 1]:
                j -= 1
                cnt += 1
                matrix[i][j] = cnt

            # up
            while i > 0 and not matrix[i - 1][j]:
                i -= 1
                cnt += 1
                matrix[i][j] = cnt

        return matrix