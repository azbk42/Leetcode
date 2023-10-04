class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        tab = []
        for i in candies:
            if i + extraCandies >= max_candie:
                tab.append(True)
            else:
                tab.append(False)
        return tab
