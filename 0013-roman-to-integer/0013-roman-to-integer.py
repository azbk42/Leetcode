class Solution:
    def romanToInt(self, s: str) -> int:
        letter = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and letter[s[i]] < letter[s[i + 1]]:
                result = result - letter[s[i]]
            else:
                result = result + letter[s[i]]
        return result 