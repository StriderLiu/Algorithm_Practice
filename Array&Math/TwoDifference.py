# Input: numbers={1, 5, 3, 4, 2, 7, 5}, k=2
# Output: 6 (number of pairs)

class Solution(object):
    # The brilliant usage of Dictionary!!!!!!
    def twoDiff(self, a, k):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        d = {}

        for i in range(len(a)):
            d[a[i]] = 0
        for i in range(len(a)):
            if a[i] + k in d.keys():
                count += 1
            if a[i] - k > 0 and a[i] - k in d.keys():
                count += 1

        return int(count / 2)
        # for i in range(len(a)):
        #     if a[i] in d.keys():
        #         count += 1
        #
        #     if a[i] - k > 0:
        #         if d[a[i] - k] is 0:
        #             d.update({d[a[i] - k]: 0})
        #         else:
        #             d[a[i] - k] += 1
        #
        #     if d[a[i] + k] is :
        #         d.update({d[a[i] + k]: 0})
        #     else:
        #         d[a[i] + k] += 1
        # return count

if __name__ == '__main__':
    # a = [1, 5, 3, 4, 2, 7, 5]
    # k = 2
    [n, k] = input().strip().split(' ')
    n = int(n)
    k = int(k)
    list = input().strip().split(' ')
    a = []
    for c in list:
        a.append(int(c))
    # if len(list) is not n:
    #     print('error')

    print(Solution().twoDiff(a, k))