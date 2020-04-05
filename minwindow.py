def minwindow(source:str,target:str):
    start = 0
    minLen = 10000
    left,right = 0,0

    window = {}
    needs = {}

    for i in target:
        if i in needs:
            needs[i] += 1
        else:
            needs[i] = 1
    
    match = 0
    while right<len(source):
        c1 = source[right]
        if c1 in needs:
            window[c1] = window[c1] + 1 if c1 in window else 1
            if needs[c1] == window[c1]:
                match+=1
        right+=1
        while match==len(needs):
            if right - left < minLen:
                start = left
                minLen = right - left

            c2 = source[left]
            if c2 in needs and needs[c2]:
                window[c2] -= 1 
                if window[c2] < needs[c2]:
                    match = match - 1
            left = left + 1
    return source[start:start + minLen] if minLen < 10000 else ""
                
            

source = 'adbccdafafe'
target = 'adc'
print("the min len is ")
print(minwindow(source,target))


def minwindow(source:str,target:str):
    res = []
    needs = {}
    window = {}
    for need in target:
        needs[need]=needs[need] + 1 if need in needs else 1
    left,right = 0,0
    match = 0
    while right<len(source):
        c1 = source[right]
        window[c1] =window[c1] + 1 if c1 in window else 1
        if c1 in  needs and window[c1] == needs[c1]:
            match += 1
        right+=1

        while match == len(needs):
            if right - left == len(target):
                res.append(left)

            c2 = source[left]
            if c2 in window:
                window[c2]-=1
                if c2 in needs and window[c2]<needs[c2]:
                    match -=1
            left+=1

    return res

source = 'adbccdafafe'
target = 'adc'
print("the yiwie is ")
print(minwindow(source,target))

def minwindow(source:str):
    left,right = 0,0
    windowdict = {}
    res = 0
    while right < len(source):
        name = source[right]
        windowdict[name]=windowdict[name]+1 if name in windowdict else 1
        right += 1
        while windowdict[name] >1:
            c2 = source[left]
            windowdict[c2] -= 1
            left += 1
        res = max(res,right-left)
    return res
print(minwindow("abccdefd"))





        