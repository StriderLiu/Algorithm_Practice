# Given an array of integers, find two numbers such that they add up
# to a specific target number.

# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
class Solution(object):
    # The brilliant usage of Dictionary!!!!!!
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                return [d.get(nums[i])+1, i+1]
            else:
                d[target-nums[i]] = i

if __name__ == '__main__':
    nums = [3, 2, 4, 8, 8, 5]
    target = 9
    print(Solution().twoSum(nums, target))