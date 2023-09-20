class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majoriity = len(nums) // 2
        i = 0
        nb_set = set()
        while i < len(nums):
            if nums[i] in nb_set:
                i += 1
            if nums.count(nums[i]) > majoriity:
                return nums[i]
            else:
                nb_set.add(nums[i])
                i += 1