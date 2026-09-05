class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '':
            return 0
        res = ''
        f = 0
        
        if s[0] == '-':
            f = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for c in s:
            if '0' <= c <= '9':
                res += c
            else:
                break

        if res == '':
            return 0

        num = int(res)
        
        if f:
            num = -num
        
        if num < -2**(31):
            num = -2**(31)
        elif num > 2**(31)-1:
            num = 2**(31)-1
        return num
