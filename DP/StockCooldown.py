class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        # # O(n) space DP solution
        # profit, cd = [0 for i in range(n)], -1
        # for i in range(1, n):
        #     if prices[i] > prices[i - 1]:
        #         if i - 1 == cd:
        #             profit[i] = max(profit[cd - 2] + prices[i] - prices[cd],
        #                             profit[cd - 1] + max(prices[i] - prices[cd - 1], 0))
        #         else:
        #             profit[i] = profit[i - 1] + prices[i] - prices[i - 1]
        #
        #         if i < n - 1 and prices[i] > prices[i + 1]:
        #             cd = i + 1
        #     else:
        #         profit[i] = profit[i - 1]
        #
        # return profit[n - 1]

        # O(1) space
        profit, cd = 0, -1
        pre1, pre2, pre3 = 0, 0, 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                if i - 1 == cd:
                    profit = max(pre3 + prices[i] - prices[cd], pre2 + max(prices[i] - prices[cd - 1], 0))
                else:
                    profit += prices[i] - prices[i - 1]

                if i < n - 1 and prices[i] > prices[i + 1]:
                    cd = i + 1
            pre3 = pre2
            pre2 = pre1
            pre1 = profit

        return profit