class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix is None:
            return []

        m, n, i, j = len(matrix), len(matrix[0]), 0, 0
        T = [[True for x in range(n)] for x in range(m)]
        
        result = [matrix[0][0]]
        T[0][0] = False

        while len(result) < m * n:
            # move right
            while j < n - 1 and T[i][j + 1]:
                j += 1
                result.append(matrix[i][j])
                T[i][j] = False

            # move down
            while i < m - 1 and T[i + 1][j]:
                i += 1
                result.append(matrix[i][j])
                T[i][j] = False

            # move left
            while j > 0 and T[i][j - 1]:
                j -= 1
                result.append(matrix[i][j])
                T[i][j] = False

            # move up
            while i > 0 and T[i - 1][j]:
                i -= 1
                result.append(matrix[i][j])
                T[i][j] = False

        return result

# matrix = [
#             [1, 2, 3, 4, 5],
#             [6, 7, 8, 9, 10],
#             [11, 12, 13, 14, 15]
# ]

matrix = []
print(Solution().spiralOrder(matrix))