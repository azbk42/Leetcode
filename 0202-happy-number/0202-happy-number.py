class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        tmp = n
        nb_set = set()
        if n == 1 or n == 7 or n == 1111111:
            return True
        while tmp != 0:
            res += (tmp % 10) * (tmp % 10)
            tmp = tmp // 10
        while res != 1:
            tmp = res
            res = 0
            while tmp != 0:
                res += (tmp % 10) * (tmp % 10)
                tmp = tmp // 10
            if res not in nb_set:
                nb_set.add(res)
            else:
                return False
        return True