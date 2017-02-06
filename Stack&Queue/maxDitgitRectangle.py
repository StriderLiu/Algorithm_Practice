class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rLen, cLen = len(matrix), len(matrix[0])
        heights = [0 for i in range(cLen)]
        heights.append(-1)
        maxArea = 0

        for row in range(rLen):
            for col in range(cLen):
                matrix[row][col] = int(matrix[row][col])

        for row in range(rLen):
            stack = [-1]
            for i in range(cLen + 1):
                if i < cLen:
                    if not matrix[row][i]:
                        heights[i] = 0
                    else:
                        heights[i] += 1

                while heights[i] < heights[stack[-1]]:
                    top = stack.pop()
                    maxArea = max(maxArea, heights[top] * (i - stack[-1] - 1))
                stack.append(i)

        return maxArea