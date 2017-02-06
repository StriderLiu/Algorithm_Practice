class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt, prime = 0, self.allPrimes(n)
        for i in range(2, n):
            if prime[i]:
                cnt += 1
        return cnt

    # Sieve of Eratosthenes
    def allPrimes(self, n):
        prime = [False for i in range(n)]
        for i in range(2, n):
            prime[i] = True
        i = 2
        while i * i < n:
            if not prime[i]:
                i += 1
                continue
            for j in range(i * i, n, i):
                prime[j] = False
            i += 1
        return prime

    # def isPrime(self, n):
    #     if n <= 1:
    #         return False
    #     # Loop's ending condition is i * i <= num instead of i <= sqrt(num)
    #     # to avoid repeatedly calling an expensive function sqrt()
    #     i = 2
    #     while i * i <= n:
    #         if not n % i:
    #             return False
    #     return True

print(Solution().countPrimes(100))