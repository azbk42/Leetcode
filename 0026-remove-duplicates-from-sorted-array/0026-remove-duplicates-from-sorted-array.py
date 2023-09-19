class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        len_nums = len(nums)
        while i < len_nums - 1:
            if nums[i+1] == nums[i]:
                del nums[i+1]
                len_nums -= 1
            else:
                i += 1
        return len(nums)