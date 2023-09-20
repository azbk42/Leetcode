class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txt = s[::-1]
        i = 0
        count = 0
        while i < len(txt) and txt[i] == ' ':
            i += 1
        while i < len(txt) and txt[i] != ' ':
            i += 1
            count += 1
        return count
