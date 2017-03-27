class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(A) or not len(B) or not len(B[0]):
            return []

        # # TLE
        # hash = {}
        # rowA, colA, colB = len(A), len(A[0]), len(B[0])
        # for i in range(rowA):
        #     for j in range(colB):
        #         for k in range(colA):
        #             if not A[i][k] or not B[k][j]:
        #                 continue
        #             if (i, j) not in hash:
        #                 hash[(i, j)] = A[i][k] * B[k][j]
        #             else:
        #                 hash[(i, j)] += A[i][k] * B[k][j]
        # res = [[0 for i in range(colB)] for j in range(rowA)]
        # for (i, j) in hash:
        #     res[i][j] = hash[(i, j)]
        # return res

        # # 169ms (better!)
        # valsA = []
        # rowA, colA, colB = len(A), len(A[0]), len(B[0])
        # for i in range(rowA):
        #     valsRow = []
        #     for j in range(colA):
        #         if not A[i][j]:
        #             continue
        #         valsRow.append((j, A[i][j]))
        #     valsA.append(valsRow)
        #
        # res = [[0 for i in range(colB)] for j in range(rowA)]
        # for i in range(rowA):
        #     for j in range(len(valsA[i])):
        #         for k in range(colB):
        #             res[i][k] += valsA[i][j][1] * B[valsA[i][j][0]][k]
        #
        # return res

        # Or do it this way
        rowA, colA, colB = len(A), len(A[0]), len(B[0])
        res = [[0 for i in range(colB)] for j in range(rowA)]
        for i in range(rowA):
            for j in range(colA):
                if not A[i][j]:
                    continue
                for k in range(colB):
                    if not B[j][k]:
                        continue
                    res[i][k] += A[i][j] * B[j][k]

        return res

A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,1,1],[1,1,1],[1,1,1]]
print(Solution().multiply(A, B))

