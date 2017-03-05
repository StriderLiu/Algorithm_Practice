class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
        for i, cur in enumerate(prices):
            sell2 = max(sell2, cur + buy2)
            buy2 = max(buy2, -cur + sell1)
            sell1 = max(sell1, cur + buy1)
            buy1 = max(buy1, -cur)
        return sell2