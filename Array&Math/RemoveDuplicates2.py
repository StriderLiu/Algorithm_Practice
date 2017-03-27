class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n

        length, cnt = 0, 0
        for i in range(n):

            if not i or nums[i] == nums[i - 1]:
                cnt += 1
                if cnt <= 2:
                    length += 1
            else:
                nums[length] = nums[i]
                cnt = 1
                length += 1

        return length

nums = [1, 1, 1, 2, 2, 2, 2, 3]
print(Solution().removeDuplicates(nums))
print(nums)