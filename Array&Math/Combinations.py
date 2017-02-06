# Given two integers n and k,
# return all possible combinations of k numbers out of 1 ... n.
# For example,
# If n = 4 and k = 2, a solution is:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    flags = []
    # Convert the problem to an equivalent one
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        list = []
        c0 = 0
        c1 = 0
        self.suffix(list, n, k, c0, c1)

        # Solution.flags.reverse()
        for l in Solution.flags:
            temp = []
            for i in range(n):
                if l[i]:
                   temp.append(i+1)

            result.append(temp)

        return result

    def suffix(self, list, n, k, c0, c1):
        if c0 is n-k:
            while len(list) < n:
                list.append(1)
            Solution.flags.append(list)
        elif c1 is k:
            while len(list) < n:
                list.append(0)
            Solution.flags.append(list)
        else:
            list0 = list[:]
            list0.append(0)
            list1 = list[:]
            list1.append(1)
            self.suffix(list0, n, k, c0+1, c1)
            self.suffix(list1, n, k, c0, c1+1)

if __name__ == '__main__':
    print(Solution().combine(2, 1))