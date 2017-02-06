class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        # maxPro stores the result that is the max we have found so far
        # imax/imin stores the max/min product of subarray that ends with the current number
        maxPro, imax, imin = nums[0], nums[0], nums[0]
        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                imax, imin = imin, imax

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)

            # the newly computed max value is a candidate for our global result
            maxPro = max(maxPro, imax)

        return maxPro