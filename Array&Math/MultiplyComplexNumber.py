class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ind1, ind2 = a.index('+'), a.index('i')
        a1, a2 = int(a[: ind1]), int(a[ind1 + 1 : ind2])
        ind1, ind2 = b.index('+'), b.index('i')
        b1, b2 = int(b[: ind1]), int(b[ind1 + 1 : ind2])
        return str(a1 * b1 - a2 * b2) + '+' + str(a2 * b1 + a1 * b2) + 'i'