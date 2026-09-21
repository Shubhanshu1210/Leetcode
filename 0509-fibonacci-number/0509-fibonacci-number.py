class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        for i in range(2,n+1):
            n = a + b
            a = b
            b = n
        return n