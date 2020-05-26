def palindrome(s,l,r):
    while  l>= 0 and r < len(s) and s[l]==s[r]:
        l -= 1
        r += 1
    return s[int(l+1):int(r)]

def longestPalindrome(s):
    res = ""
    for i in range(0,len(s)):
        s1 = palindrome(s,i,i)
        s2 = palindrome(s,i,i+1)
        res = res if len(res)>len(s1) else s1
        res = res if len(res)>len(s2) else s2
    return res


if __name__ == '__main__':
    s_test = "abccba488"
    print(longestPalindrome(s_test))