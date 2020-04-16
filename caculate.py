def string2int(s):
    n = 0
    for i in range(0,len(s)):
        n = 10*n + int(s[i])
    return n

def caculate(s:str):
    stk = []
    num = 0
    sign = '+'
    for i in range(0,len(s)):
        c = s[i]
        if c.isdigit():
            num = 10*num + int(c)
            # print(num)
        # print(c)
        if not c.isdigit() or i == len(s) - 1:
            if sign == '+':
                stk.append(num)
            if sign == '-':
                stk.append(-num)
            if sign == '*':
                pre = stk.pop()
                stk.append(pre*num)
            if sign == '/':
                pre = stk.pop()
                stk.append(pre/num)

            sign = c
            num = 0
    print(stk)
    res = 0 
    while len(stk)>0:
        res += stk.pop()
    return res

def caculate(s:str):
    def helper(s):
        stk = []
        num = 0
        sign = '+'
        while len(s)>0:
            c = s.pop(0)
            print(c)
        # c = s[i]
            if c.isdigit():
                num = 10*num + int(c)
            if c == '(':
                num = helper(s)

            if not c.isdigit() or len(s)==0:
                if sign == '+':
                    stk.append(num)
                if sign == '-':
                    stk.append(-num)
                if sign == '*':
                    pre = stk.pop()
                    stk.append(pre*num)
                if sign == '/':
                    pre = stk.pop()
                    stk.append(pre/num)

                sign = c
                num = 0
            if c == ')':
                break
        print(stk)
        res = 0 
        while len(stk)>0:
            res += stk.pop()
        return res
    return helper(list(s))




if __name__ == '__main__':
    s = "1+(2-3)*4/2"
    print(caculate(s))