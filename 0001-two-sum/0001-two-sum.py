class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = 0
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hashmap:
                return [i, hashmap[res]]
            else:
                hashmap[nums[i]] = i
        return []
        