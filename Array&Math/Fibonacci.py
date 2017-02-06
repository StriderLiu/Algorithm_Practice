# F(n) = F(n-1) + F(n-2)
# F(1) = F(2) = 1
# Dynamic Programming is required
class Fibonacci(object):
    @staticmethod
    def run(n):
        result = 1
        f1 = 1
        f2 = 1

        print('1 ')

        if n < 2:
            return 1

        for i in range(2, n):
            result = f1 + f2
            f1 = f2
            f2 = result
            print(str(result) + ' ')

        return result

if __name__ == '__main__':
    result = Fibonacci.run(int(input('Enter the number n:')))