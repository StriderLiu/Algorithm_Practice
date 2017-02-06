# Only one transaction
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        minPri, maxPro = sys.maxsize, 0

        for i in range(n):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i] - minPri)
        return maxPro

print(Solution().maxProfit([7,1,5,3,6,4]))