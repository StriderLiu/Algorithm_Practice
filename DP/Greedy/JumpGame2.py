class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # DP
        # O(n^2) Time -- TLE, O(n) Space
        # minSteps = [float('inf') for i in range(n)]
        # minSteps[0] = 0
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] >= i - j:
        #             minSteps[i] = min(minSteps[i], minSteps[j] + 1)
        #             break
        # return minSteps[n - 1]

        # Greedy
        # O(n) Time, O(1) Space
        maxReach, edge, steps = 0, 0, 0
        for i in range(n - 1):
            maxReach = max(maxReach, nums[i] + i)
            if i == edge:
                steps += 1
                edge = maxReach
                if edge >= n - 1:
                    break
        return steps

