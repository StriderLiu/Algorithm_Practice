class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) < 2:
        #     return nums[0]
        # hash = {}
        # for m in nums:
        #     if m not in hash:
        #         hash[m] = 1
        #     else:
        #         hash[m] += 1
        # for k in hash:
        #     if hash[k] < 2:
        #         return k

        # O(1) Space
        # We use bitwise XOR to solve this problem :
        # 0 ^ N = N
        # N ^ N = 0
        # and bitwise operation is commutative

        # So..... if N is the single number
        #
        # N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N
        #
        # = (N1^N1) ^ (N2^N2) ^..............^ (Nx^Nx) ^ N
        #
        # = 0 ^ 0 ^ ..........^ 0 ^ N
        #
        # = N

        res = 0
        for m in nums:
            res ^= m
        return res