class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        count = 0
        array = []
        for i in digits:
            res = res * 10 + i
        res += 1
        for i in range(len(str(res))):
            array.append(res % 10)
            res = res // 10
        array.reverse()
        return array
