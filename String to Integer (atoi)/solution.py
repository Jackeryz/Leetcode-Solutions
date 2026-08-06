
        num = int(res)
        
        if f:
            num = -num
        
        if num < -2**(31):
            num = -2**(31)
        elif num > 2**(31)-1:
            num = 2**(31)-1
        return num
