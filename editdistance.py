# 将s1 变成s2进行举例
def minDistance(s1,s2)->int:
    def dp(i,j):
        # base case
        if i == -1:
            return j + 1 
        if j == -1:
            return i + 1
        if s1[i] == s2[j]:
            return dp(i - 1, j -1)
        else:
            return min(dp(i,j-1) + 1 , # insert
                       dp(i - 1,j) + 1,# delete
                       dp(i - 1, j-1) + 1 # replace
                )
    return dp(len(s1)-1,len(s2) - 1)


def min_distance_dynamic_memo(s1,s2)->int:
    memo = dict()
    def dp(i,j):
        # base case
        # if (i,j) in memo:
            # return memo[(i,j)]
        if i == -1:
            return j + 1 
        if j == -1:
            return i + 1
        if s1[i] == s2[j]:
            # memo()
            return dp(i - 1, j -1)
        else:
            return min(dp(i,j-1) + 1 , # insert
                       dp(i - 1,j) + 1,# delete
                       dp(i - 1, j-1) + 1 # replace
                )
    return dp(len(s1)-1,len(s2) - 1)


def min_distance_dynamic_dp(s1,s2)->int:
    m,n = len(s1),len(s2)
    dp = [[0]*(m+1)]*(n+1)
    print(dp)
    # base case
    for i in range(1,m+1):
        dp[i][0] = i
        print(dp[0][0])
    for j in range(1,n+1):
        dp[0][j] = j
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j]+1,
                    dp[i][j-1]+1,
                    dp[i-1][j-1]+1)
    print(dp)
    return dp[m-1][n-1]

    
if __name__ == '__main__':
    s1 = 'acd'
    s2 = 'abc'
    print(minDistance(s1,s2))
    print(min_distance_dynamic_dp(s1,s2))