import sys
from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # # DP
        # f = [sys.maxsize for i in range(n + 1)]
        # f[0] = 0
        # for i in range(1, n + 1):
        #     j = 1
        #     while j * j <= i:
        #         f[i] = min(f[i], f[i - j * j] + 1)
        #         j += 1
        # return f[n]

        # Static DP
        # dp = [0]
        # while len(dp) <= n:
        #     size, curtMin = len(dp), sys.maxsize
        #     j = 1
        #     while j * j <= size:
        #         curtMin = min(curtMin, dp[size - j * j] + 1)
        #         j += 1
        #     dp += [curtMin]
        #
        #     # Let's do it more pythonic!!!
        #     dp += [min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5) + 1)) + 1]
        # return dp[n]

        # # BFS
        # # **Risk** Memory Limit Exeeded (when n is large)
        # if n < 4:
        #     return n
        # squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        # cnt, que = 0, deque([n])
        #
        # while que:
        #     size = len(que)
        #     cnt += 1 # cnt plus 1 for each level
        #     # use the idea of level order traversal by limiting the number of pop operation
        #     for i in range(size):
        #         curt = que.popleft()
        #         for square in squares:
        #             if square > curt:
        #                 break
        #             if square == curt: # First time the number is reduced to zero
        #                 return cnt
        #             que.append(curt - square)
        #
        # return cnt

        # Better BFS (less memory cost)
        if n < 4:
            return n
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        cnt, toCheck = 0, {n}

        while toCheck:
            cnt += 1
            tmp = set()
            for curt in toCheck:
                for square in squares:
                    if square > curt:
                        break
                    if square == curt:
                        return cnt
                    tmp.add(curt - square)
            toCheck = tmp

        return cnt


print(Solution().numSquares(1535))