class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n, res = len(nums), []
        if not n:
            if upper == lower:
                res.append(str(lower))
            elif upper > lower:
                res.append(str(lower) + '->' + str(upper))
            return res

        if nums[0] == lower + 1:
            res.append(str(lower))
        elif nums[0] > lower + 1:
            res.append(str(lower) + '->' + str(nums[0] - 1))

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 2:
                res.append(str(nums[i - 1] + 1))
            elif nums[i] > nums[i - 1] + 1:
                res.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))

        if upper == nums[n - 1] + 1:
            res.append(str(upper))
        elif upper > nums[n - 1] + 1:
            res.append(str(nums[n - 1] + 1) + '->' + str(upper))
        return res