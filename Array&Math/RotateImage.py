# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for m in range(n, 1, -2):
            i = int((n - m) / 2 )# must transfer to integer

            tmp1 = [row[m + i - 1] for row in matrix[i:(m + i)]]
            list.reverse(tmp1)
            tmp2 = matrix[m + i - 1][i:(m + i)]
            tmp3 = [row[i] for row in matrix[i:(m + i)]]
            list.reverse(tmp3)
            
            for j in range(i, m + i):
                matrix[j][m + i - 1] = matrix[i][j]
            
            matrix[m + i - 1][i:(m + i)] = tmp1[:]

            for j in range(i, m + i):
                matrix[j][i] = tmp2[j - i]
            
            matrix[i][i:(m + i)] = tmp3[:]
            
matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

# matrix = [
#             [1, 2],
#             [3, 4]
#           ]



Solution().rotate(matrix)

for l in matrix:
    print(l)
