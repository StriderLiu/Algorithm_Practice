# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        if n < 2:
            return 0
            
        maxArea = 0
#         # This solution is too slow (O(n^2)), think hard!
#         # Do we really have to know all the max values (for each elems)?
        
#         for i in range(n):
#             j, k = 0, n - 1
#             
#             while height[j] < height[i]:
#                 j += 1
#             while height[k] < height[i]:
#                 k -= 1
#             
#             maxArea = max(maxArea, height[i] * max(i - j, k - i))
        
        # Now jump out of the circle and try to think like this:
        # We can calculate the widest container, right?
        
        # Since all other possible containers are less wide, so to hold more water,
        # they need to be higher.
        # Thus, after evaluating that widest container,
        # skip lines at both ends that don't support a higher height. 
        i, j = 0, n - 1
        while i < j:
            h = min(height[i], height[j])
            maxArea = max(maxArea, h * (j - i))
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
            
        return maxArea
        
# height = [1, 2, 1]
# height = [2, 4, 3, 6, 0, 0, 0, 0, 2, 8]
# height = [5, 3, 4, 0, 60, 50, 2, 4]
height = range(15000)
print(Solution().maxArea(height))