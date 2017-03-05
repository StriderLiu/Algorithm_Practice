class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k:
            return 0
        if k > len(prices) / 2: # if k is too large, then this becomes stock2
            return self.greedy(prices)

        curMax = [0 for i in range(2 * k)] # O(k) Space
        for i in range(2 * k):
            if not i % 2:
                curMax[i] = float('-inf')

        for curt in prices: # O(n * k) Time
            for j in range(2 * k - 1, 0, -1):
                if j % 2 != 0:
                    curMax[j] = max(curMax[j], curt + curMax[j - 1])
                else:
                    curMax[j] = max(curMax[j], -curt + curMax[j - 1])
            curMax[0] = max(curMax[0], -curt)
        return curMax[2 * k - 1]

    def greedy(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


k = 2
prices = []
print(Solution().maxProfit(k, prices))