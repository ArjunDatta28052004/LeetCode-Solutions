class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        a = str(abs(x))
        a = a[::-1]
        num = sign * int(a)
        if -(2**31) <= num <= (2**31) - 1:
            return num
        else:
            return 0
