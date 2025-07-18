class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            m = [0]*(n+1)
            m[0] = 0
            m[1] = 1
            for i in range(2,n+1):
                m[i] = m[i-1] + m[i-2]
        return m[n]
        
