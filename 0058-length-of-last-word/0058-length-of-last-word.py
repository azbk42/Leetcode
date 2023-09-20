class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        tmp = 0
        i = 0
        count = 0
        while i < len(s):
            if s[i] != ' ':
                if not word:
                    tmp = i
                    word = 1
            else:
                word = 0
            i += 1
        while tmp < len(s) and s[tmp] != ' ':
            count += 1
            tmp += 1
        return count