class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_nums = len(nums)

        k = k % len_nums
        for i in range(k):
            elem = nums.pop()
            nums.insert(0, elem)
        