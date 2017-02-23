class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # O(n) Time, O(n) Space
        # # descending stack (count by horizontal strip)
        # area, stack, n = 0, [], len(height)
        # for i in range(n):
        #     while stack and height[i] > height[stack[-1]]:
        #         middle = stack.pop()
        #         if stack:
        #             area += (min(height[stack[-1]], height[i]) - height[middle]) * (i - stack[-1] - 1)
        #     stack.append(i)
        # return area

        # O(n) Time, O(1) Space
        # Two pointers (count by vertical bar)
        l, r, leftMax, rightMax = 0, len(height) - 1, 0, 0
        area = 0

        while l < r:
            leftMax, rightMax = max(leftMax, height[l]), max(rightMax, height[r])
            if leftMax < rightMax:
                area += leftMax - height[l]
                l += 1
            else:
                area += rightMax - height[r]
                r -= 1

        return area

height = [4, 2, 3]
print(Solution().trap(height))