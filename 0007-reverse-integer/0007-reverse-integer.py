class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1

        if x < 0:
            sign = -1
            x = -x

        while x > 0:
            rem = x % 10
            x //= 10
            if rev > 214748364 or (rev == 214748364 and rem > 7):
                return 0
            rev = rev * 10 + rem

        return sign * rev