class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea, stack = 0, [-1]
        heights.append(-1)

        i = 0
        while i < len(heights):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                ind = stack.pop()
                maxArea = max(maxArea, heights[ind] * (i - stack[-1] - 1))
        return maxArea

print(Solution().largestRectangleArea([4, 4, 4]))