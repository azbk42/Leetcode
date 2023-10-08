class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nb = set()
        for i in nums:
            if i not in set_nb:
                set_nb.add(i)
            else:
                return True
        return False