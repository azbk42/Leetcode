class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        verif = 0
        res = 0
        tmp = 0
        nb = num
        while num > 0:
            tmp = num % 10
            num = num // 10
            if tmp != 0:
                verif = 1
            if verif == 1:
                res = res * 10 + tmp
        tmp = 0
        while res > 0:
            tmp = tmp * 10 + res % 10
            res = res // 10
        if tmp == nb:
            return True
        return False