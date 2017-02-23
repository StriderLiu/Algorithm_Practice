class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        k %= n

        # # BF: O(n * (k%n)) Time; O(1) Space
        # for i in range(k):
        #     pre = nums[n - 1]
        #     for j in range(n):
        #         pre, nums[j] = nums[j], pre

        # # O(n) Time; O(n) Space
        # left, right = nums[: n - k], nums[n - k:]
        # nums[:] = right + left

        # O(n) Time; O(1) Space
        # Reverse 3 times
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

        # # O(n) Time; O(1) Space
        # # Using Cyclic Replacements
        # start, cnt = 0, 0
        # while cnt < n:
        #     cur = start
        #     pre = nums[start]
        #     while True:
        #         next = (cur + k) % n
        #         nums[next], pre = pre, nums[next]
        #         cur = next
        #         cnt += 1
        #         if start == cur:
        #             break
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)
