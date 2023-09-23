class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        verif = 0
        len_nums = len(nums)
        i = 0
        while i < len_nums - 1:
            if nums[i] == nums[i + 1]:
                if verif >= 1:
                    del nums[i + 1]
                    len_nums -= 1
                    i -= 1
                else:
                    verif += 1
            else:
                verif = 0
            i += 1
        return len_nums
