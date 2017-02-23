class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return nums
        # Boyer-Moore Majority Vote algorithm
        cnt1, cnt2, candidate1, candidate2 = 0, 0, float('inf'), float('inf')
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif not cnt1:
                candidate1, cnt1 = num, 1
            elif not cnt2:
                candidate2, cnt2 = num, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        return [num for num in (candidate1, candidate2) if nums.count(num) > n // 3]

nums = [2, 2]
print(Solution().majorityElement(nums))