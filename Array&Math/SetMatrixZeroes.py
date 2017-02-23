class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        # # O(mn) Time, O(n) Space
        # colNums = set()
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     reset = False
        #     for j in range(n):
        #         if not matrix[i][j]:
        #             colNums.add(j)
        #             reset = True
        #     if reset:
        #         for j in range(n):
        #             matrix[i][j] = 0
        #
        # for j in colNums:
        #     for i in range(m):
        #         matrix[i][j] = 0

        # O(mn) Time, O(1) Space
        # 向外映射，向内修改 (mark in place)
        # 向外降维，向内加维
        # 注意边界处理（第一行，第一列）
        m, n = len(matrix), len(matrix[0])
        clearFirstCol, clearFirstRow = False, False
        for i in range(m):
            if not matrix[i][0]:
                clearFirstCol = True
        for j in range(n):
            if not matrix[0][j]:
                clearFirstRow = True

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if not matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if not matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0

        if clearFirstCol:
            for i in range(m):
                matrix[i][0] = 0
        if clearFirstRow:
            for j in range(n):
                matrix[0][j] = 0

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
Solution().setZeroes(matrix)
print(matrix)