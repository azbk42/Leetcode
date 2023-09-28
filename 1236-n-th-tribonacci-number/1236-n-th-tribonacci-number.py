class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        nb1 = 0
        nb2 = 1
        nb3 = 1
        nb4 = 2
        while n >= 4:
            nb1 = nb2
            nb2 = nb3
            nb3 = nb4
            nb4 = nb3 + nb2 + nb1
            n -= 1
        return nb4
                    


        