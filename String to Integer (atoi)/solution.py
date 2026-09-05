class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        num = 0

        if s and s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + ord(c) - ord('0')

        num *= sign
        return max(-2**31, min(num, 2**31 - 1))
