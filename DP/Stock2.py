# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                maxPro += prices[i + 1] - prices[i]
        return maxPro

prices = [6, 1, 3, 2, 4, 7]
print(Solution().maxProfit(prices))