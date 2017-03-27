class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n, res = len(nums), set()
        # for i in range(n):
        #     if nums[i] == i + 1:
        #         continue
        #     while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
        #         tmp = nums[i]
        #         nums[i] = nums[nums[i] - 1]
        #         nums[tmp - 1] = tmp
        #     if nums[i] != i + 1:
        #         res.add(nums[i])
        # return list(res)

        # solution without swap
        # mark at the target position
        n, res = len(nums), []
        for i in range(n):
            # kind of hash function,
            # any other function also works as long as it ensures same values map to same slot
            index = abs(nums[i]) - 1 # since we can recover it, so in-place marking won't affect further checking
            if nums[index] < 0: # already has a mark which indicates another nums[i] has visited here
                res.append(index + 1)
            else: # add mark
                nums[index] *= -1
        return res
