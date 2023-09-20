class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        c = 0
        i = 0
        while i < n:
            c = b + a
            i += 1
            a = b
            b = c
        return c