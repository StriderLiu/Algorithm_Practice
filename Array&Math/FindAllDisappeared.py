class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == i + 1:
                continue
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp
        res, cnt = [], 0
        for i in range(n):
            cnt += 1
            if nums[i] != cnt:
                res.append(cnt)
        return res

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))