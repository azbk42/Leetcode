class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nb_set = set()
        for i in nums1:
            if i in nums2 and i not in nb_set:
                nb_set.add(i)
                result.append(i)
        return result