class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n, cnt = len(nums), 0
        for i in range(n):
            j, k = i + 1, n - 1
            tar = target - nums[i]
            while j < k:
                if nums[j] + nums[k] >= tar:
                    k -= 1
                else:
                    cnt += k - j
                    j += 1
        return cnt