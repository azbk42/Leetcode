class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        person = tickets[k]
        i = 0
        after = 0
        before = 0
        nb_sec = 0
        while i <= k:
            if tickets[i] > person:
                after += person
            else:
                after += tickets[i]
            i += 1
        while i < len(tickets):
            if tickets[i] >= person:
                before += person - 1
            else:
                before += tickets[i]
            i += 1
        return before + after
