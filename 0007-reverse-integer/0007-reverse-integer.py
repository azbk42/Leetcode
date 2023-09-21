class Solution:
    def reverse(self, x: int) -> int:
        minus = 1
        result = 0
        if x < 0:
            minus = -1
            x *= -1
        while x > 0:
            result = (result * 10) + (x % 10)
            x = x // 10
        if result > 2147483647:
            return 0
        return result * minus