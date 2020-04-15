def string2int(s):
    n = 0
    for i in range(0,len(s)):
        n = 10*n + int(s[i])
    return n

def caculate(s:str):
    stk = []
    num = 0
if __name__ == '__main__':
    s = "123"
    print(string2int(s))